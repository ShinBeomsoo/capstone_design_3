import os
import time
from openai import OpenAI
import json
import requests


API_KEY = os.environ["OPENAI_API_KEY_CTT"]
client = OpenAI(api_key=API_KEY)
GPT_MODEL = "gpt-3.5-turbo"


def get_mobum_data(restaurant_name: str = "", gu: str = ""):
    print(restaurant_name, gu)
    print("get mobum data")
    try:
        data = requests.get(f"http://localhost:8000/v1/mobums?name={restaurant_name}&gu={gu}", timeout=30)
        return data.json()
    except requests.exceptions.Timeout as e:
        print("Request Time out")
    except requests.exceptions.RequestException as e:
        print("request error")
    return None # data.json()


# 2. thread 생성
def create_thread(client) -> str:
    thread = client.beta.threads.create()
    return thread.id


# 3. thread에 message 추가
def add_message(client, thread, user_input: str):
    print("add message")
    client.beta.threads.messages.create(
        thread_id=thread,
        role="user",
        content=user_input,
    )


# 4. assistant 실행 객체 생성 -> 실행결과를 포함하지는 않음. 실행은 비동기적이라 완료를 기다려야함.
def create_run(client, thread):
    print("create run")
    run = client.beta.threads.runs.create(
        thread_id=thread,
        assistant_id="asst_Gb8b0dFNIhdhuVnQyLlzjZQd",
        instructions="음식점 데이터를 받아 유저에게 알려줍니다.",  # TODO: instructions 추가
    )
    return run


# 5. assistant 실행 객체의 상태를 확인하고, 완료되면 결과를 출력한다.
def run_assistants(client, thread, run):
    print("run assistants")
    count = 0
    while True:
        time.sleep(2)
        # 10번 이상 실행되었을 때
        count += 1
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id,
        )
        if count == 10:
            client.beta.threads.runs.cancel(thread_id=thread, run_id=run.id)
            return "결과값이 나오지 않았습니다. 다시 시도해보세요!"
        # run 객체의 상태가 완료되었을 때
        if run_status.status == "completed":
            print(run_status.status)
            messages = client.beta.threads.messages.list(
                thread_id=thread,
            )
            # 메시지의 마지막 메시지를 출력한다.
            return messages.data[0].content[0].text.value
        # run 객체의 상태가 requires_action일 때
        elif run_status.status == "requires_action":
            print(run_status.status)
            required_actions = (
                run_status.required_action.submit_tool_outputs.model_dump()
            )

            tool_outputs = []
            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])
                if func_name == "get_mobum_data":
                    output = get_mobum_data(arguments.get("restaurant_name", ""), arguments.get("gu", ""))
                    tool_outputs.append(
                        {
                            "tool_call_id": action["id"],
                            "output": str(output),
                        }
                    )
                else:
                    raise ValueError(f"Unknown function: {func_name}")
            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread,
                run_id=run.id,
                tool_outputs=tool_outputs,
            )

        # run 객체의 상태가 completed가 아닐 때
        else:
            time.sleep(4)