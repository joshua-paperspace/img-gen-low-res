from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from pipeline import pipe
from preprocess import imgToTensor
import requests
import io
import base64
from threading import Thread
import json
import time
from config import config


app = FastAPI()

def call_high_res_api(json_obj):
    # Will need to change the url address below
    requests.post(config.url, data=json_obj)
    return "Sent call to high res app!"

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/generate")
async def predict(prompt: str):
    image = pipe(prompt).images[0] 
    print(f"Image size: {image.size}")
    image.save("low_res.png")

    rawBytes = io.BytesIO()
    image.save(rawBytes, "PNG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())
    
    json_object = json.dumps({'init_image': str(img_base64), 'prompt': str(prompt)})
    Thread(target = call_high_res_api, args=(json_object,)).start()
    time.sleep(3)

    return FileResponse('low_res.png', media_type="image/jpeg")