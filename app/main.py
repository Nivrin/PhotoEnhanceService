from fastapi import FastAPI
from app.api import image_processing_api

app = FastAPI()

app.include_router(image_processing_api.router)
