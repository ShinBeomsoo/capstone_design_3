import os
import time
from openai import OpenAI
import json
import requests


API_KEY = os.environ["OPENAI_API_KEY_CTT"]
client = OpenAI(api_key=API_KEY)
GPT_MODEL = "gpt-3.5-turbo"


def get_current_dust(location):
    # data = requests.get(f"http://localhost:8000/dust/choongnam?sidoname={location}")
    return None  # data.json()


# 2. thread 생성
def create_thread(client) -> str:
    thread = client.beta.threads.create()
    return thread.id


# 3. thread에 message 추가
def add_message(client, thread, user_input: str):
    client.beta.threads.messages.create(
        thread_id=thread,
        role="user",
        content=user_input,
    )


# 4. assistant 실행 객체 생성 -> 실행결과를 포함하지는 않음. 실행은 비동기적이라 완료를 기다려야함.
def create_run(client, thread):
    run = client.beta.threads.runs.create(
        thread_id=thread,
        assistant_id="asst_Gb8b0dFNIhdhuVnQyLlzjZQd",
        instructions="음식점 데이터를 받아 유저에게 알려줍니다.",  # TODO: instructions 추가
    )
    return run


# 5. assistant 실행 객체의 상태를 확인하고, 완료되면 결과를 출력한다.
def run_assistants(client, thread, run):
    while True:
        time.sleep(4)
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id,
        )
        print(run_status.status)
        # run 객체의 상태가 완료되었을 때
        if run_status.status == "completed":
            messages = client.beta.threads.messages.list(
                thread_id=thread,
            )
            # 메시지의 마지막 메시지를 출력한다.
            return messages.data[0].content[0].text.value
        # run 객체의 상태가 requires_action일 때
        elif run_status.status == "requires_action":
            required_actions = (
                run_status.required_action.submit_tool_outputs.model_dump()
            )

            tool_outputs = []
            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])
                if func_name == "get_current_dust":
                    output = get_current_dust(arguments["location"])
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
