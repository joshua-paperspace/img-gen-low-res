import os
from PIL import Image
import torch
from fastapi import FastAPI, Form, File, UploadFile

# from config import config
# from resnet import resnet18, resnet34, resnet50, resnet101, resnet152, model_setup
# from preprocess import imgToTensor
from pipeline import pipe


# model = model_setup()
# prediction_classes = config.prediction_classes
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/predict")
async def predict():
    
    prompt = "a Dali-esque painting of an astronaut riding a unicorn"
    image = pipe(prompt).images[0]   
    image.save("low_res.png")
    # tensor = imgToTensor(image)

    # model.eval()
    # with torch.inference_mode():
    #     output = model(tensor)

    # _, predicted = torch.max(output.data, 1)
    # prediction = prediction_classes[predicted]

    return "Image generated"
    # return {"prediction": prediction}

    # ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]