from fastapi import FastAPI, UploadFile, File
import PyPDF2

app = FastAPI()

skills_list = [
    "python",
    "java",
    "sql",
    "machine learning",
    "aws"
]

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    
    pdf_reader = PyPDF2.PdfReader(file.file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return {"skills_found": found_skills}

