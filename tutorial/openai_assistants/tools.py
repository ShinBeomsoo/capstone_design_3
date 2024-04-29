tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_dust",
            "description": """
                시도명을 검색조건으로 하여 시도별 측정소목록에 대한
                일반 항목과 CAI최종 실시간 측정값과 지수 정보 조회 기능을 제공하는
                시도별 실시간 측정정보 조회하는 함수입니다.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "descriptoin": """
                        시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전,
                        울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북,
                        경남, 제주, 세종)으로 받는다.
                        """,
                    }
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_dust",
            "description": """
                시도명을 검색조건으로 하여 시도별 측정소목록에 대한
                일반 항목과 CAI최종 실시간 측정값과 지수 정보 조회 기능을 제공하는
                시도별 실시간 측정정보 조회하는 함수입니다.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "descriptoin": """
                        시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전,
                        울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북,
                        경남, 제주, 세종)으로 받는다.
                        """,
                    }
                },
            },
        },
    },
]
