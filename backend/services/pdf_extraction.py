import fitz  # PyMuPDF
from fastapi import UploadFile

def extract_text_from_file(file: UploadFile) -> str:
    """
    Extract text from an uploaded PDF file.
    This function is called directly from your route.
    """
    text = ""
    contents = file.file.read()  # Read the uploaded file
    with fitz.open(stream=contents, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
