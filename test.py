from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import PyPDF2

app = FastAPI()

skills_list = ["python","java","sql","machine learning","aws"]

# ---------- BEAUTIFUL WEB PAGE ----------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>AI Resume Analyzer</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:linear-gradient(135deg,#4f46e5,#9333ea);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.card{
    background:white;
    padding:40px;
    border-radius:20px;
    width:420px;
    text-align:center;
    box-shadow:0 20px 40px rgba(0,0,0,0.2);
}

h1{margin-bottom:5px;}
p{color:#666;}

button{
    margin-top:20px;
    padding:14px 25px;
    border:none;
    border-radius:10px;
    background:#4f46e5;
    color:white;
    font-size:16px;
    cursor:pointer;
}

button:hover{
    background:#4338ca;
}

.result{
    margin-top:25px;
    padding:15px;
    background:#f3f4f6;
    border-radius:10px;
    text-align:left;
}
</style>
</head>

<body>

<div class="card">

<h1>🤖 AI Resume Analyzer</h1>
<p>Upload resume and detect skills instantly</p>

<input type="file" id="fileInput">
<br>
<button onclick="upload()">Analyze Resume</button>

<div id="loading"></div>
<div id="result" class="result"></div>

</div>

<script>
async function upload(){

    let file=document.getElementById("fileInput").files[0];

    if(!file){
        alert("Please select resume");
        return;
    }

    document.getElementById("loading").innerText="Analyzing...";
    document.getElementById("result").innerText="";

    let formData=new FormData();
    formData.append("file",file);

    let response=await fetch("/upload",{
        method:"POST",
        body:formData
    });

    let data=await response.json();

    document.getElementById("loading").innerText="";
    document.getElementById("result").innerHTML=
        "<b>Skills Found:</b><br>"+data.skills_found.join(", ");
}
</script>

</body>
</html>
"""

# ---------- RESUME PROCESS ----------
@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    reader = PyPDF2.PdfReader(file.file)
    text="".join(page.extract_text() for page in reader.pages).lower()

    found=[s for s in skills_list if s in text]
    return {"skills_found": found}
