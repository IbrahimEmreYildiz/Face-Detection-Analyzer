# 🎯 Face Detection & Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat&logo=opencv)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows)

Gerçek zamanlı kamera görüntüsünden yüz tespiti yapan, tespit verilerini CSV'ye kaydeden ve Pandas ile analiz eden Python projesi.

---

## 📌 Ne Çözdü?

| Sorun | Çözüm | Sonuç |
|-------|-------|-------|
| Gerçek zamanlı yüz tespiti | OpenCV Haar Cascade (hazır model) | Saniyede ~30 kare işlendi |
| Veri kaybını önleme | 1 saniyelik aralıklarla CSV kaydı | 12 saniyede 12 kayıt, 0 veri kaybı |
| Ön yüz tespiti doğruluğu | `haarcascade_frontalface_default.xml` | Düz bakışta ~%58 tespit başarısı* |
| Veri analizi | Pandas ile ortalama/maksimum hesaplama | Anlık istatistik çıktısı |

> *Sağa/sola dönüşlerde tespit oranı düşüyor — bu Haar Cascade'in bilinen sınırlılığıdır. Cephe görüntüsünde başarı oranı daha yüksektir.

---

## 🗂️ Proje Yapısı

```
face_detection_analysis/
│
├── main.py          # Ana akış: kamera, döngü, koordinasyon
├── detector.py      # Yüz tespit ve çizim fonksiyonları
├── analyzer.py      # Pandas ile veri analizi
├── data.py          # CSV kayıt fonksiyonu
└── kayit.csv        # Otomatik oluşan veri dosyası
```

---

## 🧠 Kullanılan Teknolojiler

- **OpenCV** — Kamera akışı ve yüz tespiti (`CascadeClassifier`)
  - `haarcascade_frontalface_default.xml` modeli kullanıldı — OpenCV ile birlikte gelen **hazır eğitilmiş model**
- **NumPy** — OpenCV'nin arka planda kullandığı dizi yapısı (`frame` bir NumPy array'dir)
- **Pandas** — CSV okuma ve istatistiksel analiz
- **csv / datetime** — Zaman damgalı veri kaydı

---

## ⚙️ Kurulum

```bash
pip install opencv-python pandas
```

```bash
python main.py
```

Çıkmak için `q` tuşuna bas.

---

## 📊 Örnek Çıktı

```
kayit.csv:
2026-03-24 08:41:02.926367,1
2026-03-24 08:41:03.946461,1
2026-03-24 08:41:04.957476,0
...

Analiz:
Ortalama yüz sayısı: 0.58
Maksimum yüz sayısı: 1
```

---

## 🚀 Öğrenilen Kavramlar

- OpenCV ile gerçek zamanlı video işleme
- Haar Cascade ile nesne (yüz) tespiti
- Modüler Python yapısı (çok dosyalı proje)
- CSV ile veri kayıt ve Pandas ile analiz
- `datetime` ve `timedelta` ile zaman kontrolü
- Hata yönetimi (`try/except`)

---

## 👤 Geliştirici

**İbrahim Emre Yıldız**
[GitHub](https://github.com/IbrahimEmreYildız) • [LinkedIn](https://linkedin.com/in/ibrahimemreyildiz)
