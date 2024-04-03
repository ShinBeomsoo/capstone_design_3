import json
import os
from openai import OpenAI
import requests

API_KEY = os.environ["OPENAI_API_KEY_CTT"]
client = OpenAI(api_key=API_KEY)
GPT_MODEL = "gpt-3.5-turbo"


def chat_completion_request(
    messages, functions=None, function_call=None, model=GPT_MODEL
):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e


def get_current_dust(location):
    data = requests.get("http://localhost:8000/dust/choongnam")
    data = data.json()
    return data


functions = [
    {
        "name": "get_current_dust",
        "description": "현재 충청남도의 미세먼지 데이터를 제공합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "sidoName": {
                    "type": "string",
                    "description": "시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종) 에 대한 값입니다.",
                }
            },
            "required": ["sidoName"],
        },
    },
]

user_input = input(
    "Please enter your question here: (if you want to exit then write 'exit' or 'bye'.) "
)

while user_input.strip().lower() != "exit" and user_input.strip().lower() != "bye":
    # prompt
    messages = [
        {
            "role": "system",
            "content": "너는 미세먼지를 알려주는 봇이야. 사용자가 거주하는 '시'의 이름을 얻을 수 있어야해.",
        }
    ]
    messages.append({"role": "user", "content": user_input})

    # calling chat_completion_request to call ChatGPT completion endpoint
    chat_response = chat_completion_request(messages, functions=functions)
    print("chat_response: ", chat_response.json())

    # fetch response of ChatGPT and call the function
    assistant_message = chat_response.json()["choices"][0]["message"]
    print("assistant_message: ", assistant_message)

    print("="*30)

    if assistant_message["content"]:
        print("Assistant: ", assistant_message["content"])
        print(assistant_message)
        print("Response is: ", assistant_message["content"])
    else:
        fn_name = assistant_message["function_call"]["name"]
        arguments = assistant_message["function_call"]["arguments"]
        print("fn_name: ", fn_name, " // arguments: ", arguments)
        function = locals()[fn_name]
        print("function: ", function)
        result = function(arguments)
        print("Response is: ", result)

    user_input = input("Please enter your question here: ")
