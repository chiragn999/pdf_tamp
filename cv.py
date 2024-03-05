from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import fitz
import shutil
import os
from pprint import pprint

app = FastAPI()

@app.post("/upload-cv1")
async def upload_cv1(file: UploadFile = File(...)):
    with fitz.open(stream=await file.read(), filetype="pdf") as doc:
        metadata = doc.metadata
    return JSONResponse(content=metadata)

@app.post("/upload-cv2")
async def upload_cv2(file: UploadFile = File(...)):
    with fitz.open(stream=await file.read(), filetype="pdf") as doc:
        metadata = doc.metadata
    return JSONResponse(content=metadata)

doc1 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")
doc2 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")

pprint(doc1.metadata)
pprint(doc2.metadata)