from pydantic import BaseModel


class SendMessageSerializer(BaseModel):
    message: str
