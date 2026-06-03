# 🚀 To-Do List Manager API & DevOps Pipeline

👤 **Geliştirici:** Ahmet Gemici (170423041)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Multi--Stage-2496ED?style=for-the-badge&logo=docker)
![Coverage](https://img.shields.io/badge/Coverage-79%25-success?style=for-the-badge&logo=pytest)

---

## 📌 Proje Hakkında
Bu proje, kullanıcıların günlük görevlerini (To-Do) yönetebilmesini sağlayan, asenkron yapıda geliştirilmiş bir RESTful API'dir. Geleneksel bir backend uygulamasından farklı olarak, modern **DevOps, CI/CD ve SRE (Gözlemlenebilirlik)** pratikleri merkeze alınarak endüstri standartlarında tasarlanmıştır. 

Proje; otomatik test süreçlerini, çok aşamalı (multi-stage) konteynerizasyonu, canlı sistem izleme panellerini ve bulut veri simülasyonunu barındırır.

## 🛠️ Kullanılan Teknolojiler

| Kategori | Teknolojiler |
| :--- | :--- |
| **Backend & Veri** | FastAPI, Python 3.11, SQLAlchemy, SQLite |
| **Konteynerizasyon** | Docker, Docker Compose (Multi-stage build) |
| **CI/CD & Otomasyon**| GitHub Actions (Linting, Testing, Building) |
| **İzleme (Monitoring)**| Prometheus, Grafana |
| **Kalite Güvence (QA)** | Pytest (%79 Coverage), Selenium (E2E), k6 (p95 Latency) |
| **Bulut Simülasyonu** | LocalStack (AWS S3) |

---

## ⚙️ Kurulum ve Çalıştırma (Lokal Ortam)

Projeyi bilgisayarınızda çalıştırmadan önce **Docker Desktop**'ın kurulu ve çalışır durumda olduğundan emin olun. 

## 1. Projeyi Ayağa Kaldırma
Terminalinizi açın ve proje dizininde aşağıdaki komutu çalıştırarak tüm IT altyapısını (API, Prometheus, Grafana, LocalStack) tek seferde ayağa kaldırın:

```bash
docker-compose up -d --build
```

## 2. Sistem Bileşenlerine Erişim
Konteynerler başarıyla çalıştıktan sonra aşağıdaki bağlantılardan mikroservislere ulaşabilirsiniz:

📖 Etkileşimli API Dokümantasyonu (Swagger): http://127.0.0.1:8000/docs

📊 Grafana Canlı İzleme Paneli: http://localhost:3000 (Kullanıcı adı ve şifre: admin)

📈 Prometheus Metrikleri: http://127.0.0.1:8000/metrics

### 🧪 Test Stratejisi ve Kalite
Projede "Test Piramidi" yaklaşımı benimsenmiştir:

Kod standartları Flake8 ile denetlenmiştir.

Pytest ile %79 Test Coverage (Kapsama) oranına ulaşılmıştır.

E2E (Uçtan Uca) arayüz testleri için Selenium kullanılmıştır.

k6 kullanılarak yapılan yük testlerinde sistemin darboğaz (bottleneck) yaşamadığı raporlanmıştır (Detaylar perf/report.md dosyasındadır).

### 🎥 Canlı Demo Videosu
Projenin CI/CD süreçlerinin, canlı API kullanımının ve Grafana üzerindeki anlık metrik izlemelerinin yer aldığı uygulamalı demo videosuna aşağıdan ulaşabilirsiniz:

▶️ **[Proje Demo Videosunu İzlemek İçin Tıklayın](https://youtu.be/l25AeHkklAM)**
