# Contains only the minimum required items, and the rest are default values
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

ENV ES=<locals>
ENV JWT_SECRET_KEY=randomkey
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=<USER>
ENV MYSQL_PASS=<PASSWORD>
ENV MYSQL_DB=tep
ENV STMP_USER=<USER>
ENV STMP_PASS=<MAILPASS>
ENV LOG_EMAIL_SENDER=<admin>

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--lifespan", "on", "--log-config", "uvicorn_log.yaml"]
