# main.py

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import subprocess
import os
import time

tmp_file_dir = "/tmp/example-files"
Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get(
    path="/prompt/{prompt}",
    response_class=FileResponse,
)
async def generate_speech(prompt:str):
    subprocess.run(['./generate_speech.sh',str(prompt)])
    with open(os.path.join(tmp_file_dir, 'test1.wav'), 'wb') as disk_file:
        while not os.path.exists('test1.wav'):
            time.sleep(1)
        file = open("test1.wav","rb")
        file_bytes = file.read()

        disk_file.write(file_bytes)

        return FileResponse(disk_file.name, media_type="audio/wav")
