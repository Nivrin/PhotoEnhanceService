# app/api/image.py
from fastapi import APIRouter, UploadFile
from app.core.image_processing import process_image
from app.models.image_models import ProcessedImage
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/process_image/")
async def process_uploaded_image(file: UploadFile):
    try:
        processed_image_data = process_image(file)
        return ProcessedImage(**processed_image_data)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)})
