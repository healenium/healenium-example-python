from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Union


class Node(BaseModel):
    tag: str = ""
    id: str = ""
    classes: List[str] = Field(default_factory=list)
    index: Optional[int] = None
    other_attributes: Dict[str, str] = Field(default_factory=dict, alias="other")
    inner_text: str = Field("", alias="innerText")

    class Config:
        allow_population_by_field_name = True

    @validator("classes", pre=True)
    def split_classes(cls, value: Union[str, List[str]]) -> List[str]:
        if isinstance(value, str):
            return value.split()
        return value
