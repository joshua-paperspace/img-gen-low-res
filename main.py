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


app = FastAPI()


def call_high_res_api(json_obj):
    dictToSend = json_obj

    requests.post("http://0.0.0.0:8001/generate",json=dictToSend, headers = {'content-type': 'application/json'})

    return "Done!"


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/generate")
async def predict(prompt: str):
    # image = pipe(prompt).images[0]

    # print(type(init_image))

    # image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images[0]
    image = pipe(prompt).images[0] 
    image.save("low_res.png")

    rawBytes = io.BytesIO()
    image.save(rawBytes, "png")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())
    
    json_object = json.dumps({'init_image':str(img_base64), 'prompt':str(prompt)})
    Thread(target = call_high_res_api, args=(json_object,)).start()
    time.sleep(3)
    
    # return jsonify({'userID': userID, 'generated_img':str(img_base64)})

    return FileResponse('low_res.png', media_type="image/jpeg")


    # images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images