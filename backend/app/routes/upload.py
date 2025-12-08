from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/internal-doc")
async def upload_document(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "Upload implementation pending"}
