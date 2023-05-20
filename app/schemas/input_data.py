from pydantic import BaseModel


class InputData(BaseModel):
    ip: str
