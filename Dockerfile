FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV DATABASE_URL=postgresql://ritik:1234@localhost:5432/dynamicJobs

CMD gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
