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
                        "descriptoin": "시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종)",
                    }
                },
            },
        },
    },
]


def get_current_dust(location):
    data = requests.get(f"http://localhost:8000/dust/choongnam?sidoname={location}")
    data = data.json()
    return data


def main():
    user_prompt = input("질문을 입력하세요: ")

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
    print(completion.choices[0].message.content)
    # args = completion.choices[0].message.tool_calls[0].function.arguments
    # parse_args = json.loads(args)
    # api_result = get_current_dust(parse_args["location"])
    # print("args: ", args)
    # print("parse_args: ", parse_args)
    # print("api_result: ", api_result)

    netural_response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "user", "content": str(api_result)},
        ],
    )
    print("netural_response: ", netural_response.choices[0].message.content)


main()
