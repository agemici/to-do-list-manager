# 1. Aşama: Gerekli paketlerin kurulduğu "builder" aşaması
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 2. Aşama: Uygulamanın çalıştığı ve boyutun küçüldüğü "runner" aşaması
FROM python:3.11-slim AS runner
WORKDIR /app

# Sadece gerekli olan dosyaları ilk aşamadan kopyalıyoruz
COPY --from=builder /root/.local /root/.local
COPY ./src /app/src

# Python'un kopyalanan paketleri bulabilmesi için yol ayarı
ENV PATH=/root/.local/bin:$PATH

# Uygulamamızı 8000 portunda dışarı açıyoruz
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]