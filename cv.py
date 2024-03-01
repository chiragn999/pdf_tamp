from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import fitz
import io
from pprint import pprint

app = FastAPI()

@app.post("/upload1")
async def upload_file1(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_stream = io.BytesIO(contents)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    return JSONResponse(content=doc.metadata)

@app.post("/upload2")
async def upload_file2(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_stream = io.BytesIO(contents)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    return JSONResponse(content=doc.metadata)

doc1 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")
doc2 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")

pprint(doc1.metadata)
pprint(doc2.metadata)