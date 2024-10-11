FROM ultralytics/ultralytics:latest

WORKDIR /app

RUN pip install opencv-python

COPY . /app/

CMD ["python", "detect.py"]
