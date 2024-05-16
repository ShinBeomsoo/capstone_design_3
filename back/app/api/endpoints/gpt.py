from typing import Annotated, Any

from fastapi import APIRouter, Query

from app.core.config import get_settings
from app.gpt.step import add_message, create_run, create_thread, run_assistants


router = APIRouter()


@router.get(
    path="",
    summary="gpt와 관련된 API",
    description="OpenAI assistant을 통해 답변해주는 API",
    response_description="음식점에 대한 정보로 API 통신을 하여 얻은 결과값을 OpenAI assistant가 답을 가공하여 답변해준다.",
)
async def gpt(
    thread_id: Annotated[
        str | None,
        Query(
            title="thread_id",
            description="유저가 사용하고 있는 assistant thread id값",
        ),
    ] = None,
    user_input: Annotated[
        str | None,
        Query(
            title="user_input",
            description="유저가 assistant에게 입력한 문장",
        ),
    ] = None,
) -> Any:
    client = get_settings().GPT_CLIENT
    if thread_id == None or thread_id == "":
        print("thread_id is None")    
        thread_id = create_thread(client)
    add_message(client, thread_id, user_input)
    run = create_run(client, thread_id)
    result = run_assistants(client, thread_id, run)
    return {
        "thread_id": thread_id,
        "result": result,
    }
