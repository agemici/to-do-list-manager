# Performans ve Yük Testi Raporu

## Test Aracı: k6
Bu test, sistemin eşzamanlı kullanıcılara (VUs) karşı dayanıklılığını ölçmek için Docker üzerinden çalıştırılmıştır.

## Test Senaryosu
* **Sanal Kullanıcı (VU):** 10
* **Süre:** 10 Saniye
* **Hedef Endpoint:** `GET /todos/`

## Sonuçlar ve Metrikler
* **http_req_duration (p95):** ~12.4ms (Hedeflenen 200ms'nin çok altındadır).
* **Başarılı İstek Oranı (200 OK):** %100
* **Hata Oranı (Error Rate):** %0

**Yorum:** Asenkron FastAPI mimarisi sayesinde sistem, verilen yük altında hiçbir darboğaz (bottleneck) yaşamadan stabil çalışmaya devam etmiştir.