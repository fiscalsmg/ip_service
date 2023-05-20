from pydantic import BaseModel


class outputData(BaseModel):
    ip: str
    source_country: str
