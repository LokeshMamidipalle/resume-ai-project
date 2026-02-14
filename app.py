from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import PyPDF2

app = FastAPI()

# ---------------- HOMEPAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>AI Resume Screening API is running</h1>
    <p>Upload resumes using the API docs:</p>
    <a href="/docs">Open API Docs</a>
    """

# ---------------- SKILL LIST ----------------
skills_list = [
    "python",
    "java",
    "sql",
    "machine learning",
    "aws"
]

# ---------------- UPLOAD API ----------------
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
