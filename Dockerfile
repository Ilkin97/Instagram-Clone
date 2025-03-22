# Python Image
FROM python:3.12.9

# Çalışma dizinini belirle
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodları kopyala
COPY . .

# Portu aç
EXPOSE 8000

# Server'ı başlat
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
