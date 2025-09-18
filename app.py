from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={
        "message": 'Hello Farook, You can see your dashboard reports at <a href="http://localhost:5174/" target="_blank">Dashboard</a>'
    })
