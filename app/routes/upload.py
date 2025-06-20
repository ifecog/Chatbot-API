from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import tempfile
from app.core.vector_store import create_vector_store_from_file

router = APIRouter(prefix="/api/v1/upload", tags=["Upload"])

@router.post('/')
async def upload_file(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        create_vector_store_from_file(tmp_path)
        
        os.remove(tmp_path)
        
        return {"message": f"File '{file.filename}' uploaded and embedded successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
