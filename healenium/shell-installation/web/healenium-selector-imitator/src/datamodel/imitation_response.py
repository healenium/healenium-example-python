from pydantic import BaseModel, Field
from src.selector import SelectorType


class ImitationResponseModel(BaseModel):
    selector_type: SelectorType = Field(..., alias="type")
    selector_value: str = Field(..., alias="value")

    class Config:
        allow_population_by_field_name = True
