FROM python:3.13-slim

WORKDIR /app

COPY . . 
RUN pip install flask
#RUN pip install -r requirements.txt 

CMD ["python", "app.py"]
