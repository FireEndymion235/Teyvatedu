
FROM python:3.9

WORKDIR /app


COPY requirements.txt .
ENV APP_NAME=TEPBackendAPI
ENV JWT_SECRET_KEY=randomkey
ENV APP_VERSION=0.1.0
ENV JWT_ALGORITHM=HS256


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]