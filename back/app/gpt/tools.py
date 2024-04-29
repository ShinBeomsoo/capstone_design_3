tools = [
    {
        "type": "function",
        "function": {
            "name": "get_mobum_data",
            "description": """
                모범음식점 데이터를 가져오는 함수입니다. 이 함수에는 resturant_name과 gu을 인자로 받습니다.
                """,
            "parameters": {
                "type": "object",
                "properties": {
                    "resturant_name": {
                        "type": "string",
                        "descriptoin": "음식점 이름을 이용하여 검색조건으로 사용합니다.",
                    },
                    "gu": {
                        "type": "string",
                        "descriptoin": "서울시에 있는 구를 입력 받습니다.",
                    },
                    "gu": {
                        "type": "string",
                        "descriptoin": "서울시에 있는 구를 입력 받습니다.",
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_measure_data",
            "description": """
                위생 행정 처분을 받은 음식점 데이터를 가져오는 함수입니다.
                """,
            "parameters": {
                "type": "object",
                "properties": {
                    "": {
                        "type": "string",
                        "descriptoin": """
                        """,
                    }
                },
            },
        },
    },
]
