from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/hello", response_class=HTMLResponse)
def hello():
    return """
    <p>Hello Farook, You can see your dashboard reports at 
    <a href="http://localhost:5174/" target="_blank">Dashboard</a></p>
    """
