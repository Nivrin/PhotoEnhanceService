import base64

from fastapi import UploadFile
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter

def process_image(file: UploadFile):
    try:
        input_image = Image.open(BytesIO(file.file.read()))

        # Resize the image
        upscaled_image = input_image.resize((input_image.width * 2, input_image.height * 2), Image.LANCZOS)

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(upscaled_image)
        contrast_enhanced_image = enhancer.enhance(1.5)

        # Enhance color saturation
        enhancer = ImageEnhance.Color(contrast_enhanced_image)
        beautiful_image = enhancer.enhance(1.2)

        # Sharpen the image
        sharpened_image = beautiful_image.filter(ImageFilter.SHARPEN)

        # Convert the processed image to bytes
        output_image_bytes = BytesIO()
        sharpened_image.save(output_image_bytes, format="PNG")

        # Encode the image as a base64 string
        image_base64 = base64.b64encode(output_image_bytes.getvalue()).decode()

        # Return the processed image data as a dictionary
        processed_image_data = {
            "status": "success",
            "message": "Image processed successfully",
            "image_base64": image_base64
        }

        return processed_image_data
    except Exception as e:
        raise ValueError(f"Image processing error: {str(e)}")

def encode_image_as_base64(image: Image):
    # Helper function to encode an image as base64 string
    image_bytes = BytesIO()
    image.save(image_bytes, format="PNG")
    image_base64 = base64.b64encode(image_bytes.getvalue()).decode()
    return image_base64

def decode_base64_to_image(base64_string: str):
    # Helper function to decode a base64 string to an image
    image_bytes = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_bytes))
