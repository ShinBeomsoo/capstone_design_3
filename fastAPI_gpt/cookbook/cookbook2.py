import json
import os
from openai import OpenAI
import requests

API_KEY = os.environ["OPENAI_API_KEY_CTT"]
openai = OpenAI(api_key=API_KEY)
GPT_MODEL = "gpt-3.5-turbo"


functions = [
    {
        "type": "function",
        "description": "현재 충남의 미세먼지 데이터를 제공합니다.",
        "function": {
            "name": "get_current_dust",
            "description": "현재 충남의 미세먼지 데이터를 제공하는 함수입니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "descriptoin": "사용자의 위치 정보를 입력합니다.",
                    }
                },
            },
        },
    },
]


def get_current_dust(location):
    data = requests.get("http://localhost:8000/dust/choongnam")
    data = data.json()
    return data


def main():
    user_prompt = "충남의 미세먼지 정보를 알려주세요."

    completion = openai.chat.completions.create(
        model=GPT_MODEL,
        tools=functions,
        tool_choice="auto",
        messages=[
            {
                "role": "system",
                "content": "너는 아주 도움이 되는 비서야. 유저 프롬프트를 보고 유저의 위치를 확인하고, 그에 맞는 미세먼지 정보를 제공해줘.",
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )
    args = completion.choices[0].message.tool_calls[0].function.arguments
    # print("args(string): ", args)
    parse_args = json.loads(args)
    # print("parse_args(dict): ", parse_args)
    # print(completion.choices[0].message.content)
    api_result = get_current_dust(parse_args["location"])
    # print(api_result)
    # print(type(api_result))

    netural_response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "너는 아주 도움이 되는 비서야. 유저 프롬프트를 보고 유저의 위치를 확인하고, 그에 맞는 미세먼지 정보를 제공해줘.",
            },
            {"role": "user", "content": str(api_result)},
        ],
    )
    print("netural_response: ", netural_response.choices[0].message.content)


main()
