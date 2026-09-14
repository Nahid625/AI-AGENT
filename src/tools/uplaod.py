import cloudinary.uploader
from fastapi import File, HTTPException, UploadFile


def upload_to_cloudinary(file: UploadFile = File(...)):
    try:
        result = cloudinary.uploader.upload(file.file)
        return result.get("secure_url")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cloudinary error: {str(e)}")
