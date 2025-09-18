from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={
        "message": "Hello Farook, You can see your dashboard reports",
        "dashboard_link": {
            "url": "http://localhost:5174/",
            "label": "Dashboard"
        }
    })
