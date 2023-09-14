from pydantic import BaseModel, Field
from src.node import Node
from src.selector import SelectorType


class UserSelector(BaseModel):
    type: SelectorType
    value: str


class ImitationRequestModel(BaseModel):
    user_selector: UserSelector = Field(..., alias="userSelector")
    target_node: Node = Field(..., alias="targetNode")
