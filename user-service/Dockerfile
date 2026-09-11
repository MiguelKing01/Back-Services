FROM python:3.12-slim

WORKDIR /app

COPY user-service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY user-service/ .

COPY shared/ ./shared/

COPY firebase-service-account.json ./firebase-service-account.json

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]