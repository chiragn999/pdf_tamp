from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import time
import tempfile

app = FastAPI()

@app.post("/upload-file-info")
async def upload_file_info(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        contents = await file.read()
        temp_file.write(contents)
        temp_file.flush()

    ti_c = os.path.getctime(temp_file_path)
    ti_m = os.path.getmtime(temp_file_path)
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)

    os.unlink(temp_file_path)  # Clean up the temporary file

    return JSONResponse(content={
        "file_name": file.filename,
        "created_at": c_ti,
        "last_modified_at": m_ti
    })