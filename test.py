from fastapi.responses import HTMLResponse

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
    background:linear-gradient(135deg,#667eea,#764ba2);
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
}

.card{
    background:white;
    padding:40px;
    border-radius:15px;
    width:420px;
    text-align:center;
    box-shadow:0 15px 40px rgba(0,0,0,0.2);
}

h1{margin-bottom:5px;}
p{color:#666;}

input[type=file]{
    margin-top:20px;
}

button{
    margin-top:20px;
    padding:12px 25px;
    border:none;
    border-radius:8px;
    background:#667eea;
    color:white;
    font-size:16px;
    cursor:pointer;
}

button:hover{
    background:#5563c1;
}

.result{
    margin-top:25px;
    padding:15px;
    background:#f5f5f5;
    border-radius:8px;
    text-align:left;
}

.loading{
    margin-top:15px;
    color:#667eea;
    font-weight:bold;
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

<div id="loading" class="loading"></div>
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
