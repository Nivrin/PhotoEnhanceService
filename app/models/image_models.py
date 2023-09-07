# app/models/image.py
from pydantic import BaseModel

class ProcessedImage(BaseModel):
    status: str
    message: str
    image_base64: str