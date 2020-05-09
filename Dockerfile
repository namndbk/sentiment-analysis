FROM python:3.6-slim

WORKDIR /home/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python" , "app.py"]