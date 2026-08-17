from flask import Flask, render_template

app = Flask(__name__)

drivers = [
    {
        "name": "Conrad",
        "character": "Conrad Fisher",
        "actor": "Christopher Briney",
        "status": "online",
        "area": "Cirebon Kota",
        "phone": "6289530522457",
    },
    {
        "name": "Jeremiah",
        "character": "Jeremiah Fisher",
        "actor": "Gavin Casalegno",
        "status": "online",
        "area": "Kabupaten Cirebon",
        "phone": "6285211003707",
    },
    {
        "name": "Cam",
        "character": "Cam Cameron",
        "actor": "David Iacono",
        "status": "offline",
        "area": "Kota Bandung",
        "phone": "6282249152197",
    },
    {
        "name": "Steven",
        "character": "Steven Conklin",
        "actor": "Sean Kaufman",
        "status": "offline",
        "area": "Kabupaten Bandung",
        "phone": "6281222729005",
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        drivers=drivers,
        admin="628891006445"
    )


if __name__ == "__main__":
    app.run(debug=True)