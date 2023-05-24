FROM paperspace/fastapi-deployment:latest

WORKDIR /app

COPY main.py pipeline.py preprocess.py requirements.txt ./
COPY config ./config

RUN pip3 install -U pip && pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]