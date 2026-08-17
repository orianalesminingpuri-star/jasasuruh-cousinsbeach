from flask import Flask, render_template
app = Flask(__name__)

# ===== GANTI DATA DI SINI =====
SITE_NAME = "Jasasuruh.Cousinsbeach"
TAGLINE = "Butuh disuruh? Kami yang jalan."
DESCRIPTION = "Jasa suruh, titip, ambil, dan antar untuk memudahkan aktivitasmu."
WHATSAPP = "6281234567890"
INSTAGRAM = "https://instagram.com/usernamekamu"
TIKTOK = "https://www.tiktok.com/@usernamekamu"
AREA = "Cirebon & sekitarnya"
OPENING_HOURS = "Setiap hari • 08.00–22.00"

SERVICES = [
    ("🛒", "Belanja & Titip", "Titip makanan, kebutuhan harian, dan barang lainnya."),
    ("📦", "Ambil & Antar", "Kami ambil paket atau barang lalu mengantarkannya."),
    ("📄", "Antar Dokumen", "Antar dokumen dan kebutuhan administrasi."),
    ("✨", "Jasa Lainnya", "Punya kebutuhan khusus? Ceritakan detailnya."),
]

DRIVERS = [
    {"name":"Raka","photo":"driver1.jpg","area":"Cirebon & sekitarnya","status":"Tersedia","wa":"6281234567890"},
    {"name":"Dimas","photo":"driver2.jpg","area":"Cirebon Kota","status":"Tersedia","wa":"6281234567891"},
    {"name":"Fajar","photo":"driver3.jpg","area":"Kabupaten Cirebon","status":"Offline","wa":"6281234567892"},
]

@app.route("/")
def home():
    return render_template("index.html", site_name=SITE_NAME, tagline=TAGLINE,
        description=DESCRIPTION, whatsapp=WHATSAPP, instagram=INSTAGRAM, tiktok=TIKTOK,
        area=AREA, opening_hours=OPENING_HOURS, services=SERVICES, drivers=DRIVERS)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
