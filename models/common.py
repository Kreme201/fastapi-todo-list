from pydantic import BaseModel


class ResponseDto(BaseModel):
    success: bool
