import os
import time
from openai import OpenAI
import json
import requests

from cookbook import get_current_dust


API_KEY = os.environ["OPENAI_API_KEY_CTT"]
client = OpenAI(api_key=API_KEY)
GPT_MODEL = "gpt-3.5-turbo"


def get_current_dust(location):
    print("get_current_dust: ", location)
    data = requests.get(f"http://localhost:8000/dust/choongnam?sidoname={location}")
    return data.json()


def create_assistant(client, tools, model):
    # 1. assistant 생성
    assistant = client.beta.assistants.create(
        name="미세먼지 알림 비서",
        instructions="미세먼지 알림 비서는 사용자의 위치 정보를 입력받아 해당 지역의 미세먼지 정보를 제공합니다.",
        tools=tools,
        model=model,
    )


def create_thread(client):
    # 2. thread 생성
    thread = client.beta.threads.create()
    return thread


def add_message(client, thread):
    # 3. thread에 message 추가
    content = input("User: ")
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content,
    )
    return message


def create_run(client, thread):
    # 4. assistant 실행 객체 생성 -> 실행결과를 포함하지는 않음. 실행은 비동기적이라 완료를 기다려야함.
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_EbC75rskFu8SkD4Gt5FpdWFN",  # assistant.id,
        instructions="미세먼지 알림 비서는 사용자의 위치 정보를 입력받아 해당 지역의 미세먼지 정보를 제공합니다.",
    )
    return run


def run_assistants(client, thread, run):
    print("run id: ", run.id)
    while True:
        # print("thread_id: ", thread.id)
        # print("run_id: ", run.id)
        time.sleep(4)

        # 실행 객체를 가져와서 상태를 확인합니다.
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )

        print(run_status.status)
        # print(run_status.model_dump_json(indent=4))

        if run_status.status == "completed":
            # 스레드로부터 메시지를 가져온다.
            messages = client.beta.threads.messages.list(
                thread_id=thread.id,
            )
            # 가장 최근 답변을 가져온다.
            # print(messages)
            print(f"{messages.data[0].role.capitalize()}: {messages.data[0].content[0].text.value}")
            # for msg in messages.data:
            #     role = msg.role
            #     content = msg.content[0].text.value
            #     print(f"{role.capitalize()}: {content}")
            break
        elif run_status.status == "requires_action":
            print("requires action...")
            required_actions = (
                run_status.required_action.submit_tool_outputs.model_dump()
            )
            # print("required_actions: ", required_actions)
            tool_outputs = []

            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])
                # print("arguments: ", arguments["location"])

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
                print("Submitting ouputs back to the Assistant...")
                # print(tool_outputs)
                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=tool_outputs,
                )
        else:
            print("Not completed yet. Waiting...")
            time.sleep(5)


thread = create_thread(client)
while True:
    message = add_message(client, thread)
    run = create_run(client, thread)
    run_assistants(client, thread, run)
