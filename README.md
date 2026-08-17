# Jasasuruh.Cousinsbeach — Siap Dipakai
1. Buka folder ini di VS Code.
2. Terminal > New Terminal.
3. `python -m pip install -r requirements.txt`
4. `python app.py`
5. Buka `http://127.0.0.1:5000`

## Ganti data
Edit bagian paling atas `app.py`: WhatsApp, Instagram, TikTok, area, jam, layanan, dan driver.

## Foto driver
Masukkan foto sendiri ke `static/images/` dengan nama:
- driver1.jpg
- driver2.jpg
- driver3.jpg
Jika belum ada, website memakai huruf awal nama sebagai fallback.

## Fitur
Responsive, WhatsApp, Instagram, TikTok, profil driver, tombol chat per driver, dan form pesanan yang otomatis membuat pesan WhatsApp.

`127.0.0.1` hanya untuk komputer sendiri. Untuk publik, project perlu di-deploy ke hosting Python/Flask dan bisa diberi domain.
