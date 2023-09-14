import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.datamodel import ImitationRequestModel, ImitationResponseModel
from src.selector import Selector
from src.selector_imitator import SelectorImitator, ImitationError
from src.selector_parser import ParsingError
from typing import List


app = FastAPI()


@app.exception_handler(ImitationError)
async def imitation_error_handler(
    request: Request, exc: ImitationError
) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": [{"msg": f"Unable to imitate the user selector: {exc}"}]},
    )


@app.exception_handler(ParsingError)
async def parsing_error_handler(request: Request, exc: ParsingError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": [{"msg": f"Unable to parse the user selector: {exc}"}]},
    )


@app.get("/")
def main() -> str:
    return "this is an entry point of the selector imitator"


@app.post("/imitate", response_model=List[ImitationResponseModel])
async def imitate(request: ImitationRequestModel) -> List[ImitationResponseModel]:
    user_selector = Selector.from_type_and_value(
        selector_type=request.user_selector.type, value=request.user_selector.value
    )
    imitator = SelectorImitator(user_selector, request.target_node)
    result = [
        ImitationResponseModel(
            selector_type=selector.selector_type, selector_value=str(selector)
        )
        for selector in imitator.imitate()
    ]
    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
