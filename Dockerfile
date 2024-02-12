FROM python:3.10.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000
# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]