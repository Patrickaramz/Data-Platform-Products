FROM python:3.9-slim

WORKDIR /app

# Kopiera från requirement.txt och installera bibliotek
COPY requirements.txt .

# Installerar FastApi, Uvicorn och pandas inuti containern
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera koden över till contatinern
COPY . .

# Starta applikationen
CMD ["python", "main.py"]