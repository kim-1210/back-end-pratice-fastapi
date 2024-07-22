from fastapi import FastAPI
from fastapi.responses import FileResponse #html파일 전송 가능
import uvicorn
import json

app = FastAPI()

@app.get('/')
def index():
    return "hello"

@app.get('/data')
def index():
    return {'data' : 1234}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)