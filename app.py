from flask import Flask, render_template
app = Flask(_name_)

# ===== GANTI DATA DI SINI =====
SITE_NAME = "Jasasuruh.Cousinsbeach"
TAGLINE = "Butuh bantuan? Kami yang jalan."
DESCRIPTION = "Jasa suruh, titip, ambil, dan antar untuk memudahkan aktivitasmu."
WHATSAPP = "628891006445"
INSTAGRAM = "https://www.instagram.com/jasasuruh.cousinsbeach?igsh=NjJzZTZ1bmwzcHk0"
TIKTOK = "https://www.tiktok.com/@sikmapipel5?_r=1&_t=ZS-98wn8fkLGXh"
AREA = "Cirebon & sekitarnya"
OPENING_HOURS = "Setiap hari • 08.00–22.00"

SERVICES = [
    ("🛒", "Belanja & Titip", "Titip makanan, kebutuhan harian, dan barang lainnya."),
    ("📦", "Ambil & Antar", "Kami ambil paket atau barang lalu mengantarkannya."),
    ("📄", "Antar Dokumen", "Antar dokumen dan kebutuhan administrasi."),
    ("✨", "Jasa Lainnya", "Punya kebutuhan khusus? Ceritakan detailnya."),
]

DRIVERS = [
    {"name":"Conrad","photo":"driver1.jpg","area":"Cirebon & sekitarnya","status":"Tersedia","wa":"6289530522457"},
    {"name":"Jeremiah","photo":"driver2.jpg","area":"Cirebon Kota","status":"Tersedia","wa":"6285211003707"},
    {"name":"Cam","photo":"driver3.jpg","area":"Kabupaten Cirebon","status":"Offline","wa":"6282249152197"},
]

@app.route("/")
def home():
    return render_template("index.html", site_name=SITE_NAME, tagline=TAGLINE,
        description=DESCRIPTION, whatsapp=WHATSAPP, instagram=INSTAGRAM, tiktok=TIKTOK,
        area=AREA, opening_hours=OPENING_HOURS, services=SERVICES, drivers=DRIVERS)

if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=5000)