
FROM python:3.9

WORKDIR /app


COPY requirements.txt .
ENV APP_NAME=TEPBackendAPI
ENV JWT_SECRET_KEY=randomkey
ENV APP_VERSION=0.1.0
ENV JWT_ALGORITHM=HS256
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASS=123456
ENV MYSQL_DB=tep

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]