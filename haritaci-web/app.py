from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cevap = ""
    if request.method == "POST":
        soru = request.form["soru"].lower()

        if "utm" in soru and "nedir" in soru:
            cevap = "UTM, dünya üzerindeki koordinatları düzlemde göstermek için kullanılan bir projeksiyon sistemidir."
        elif "ed50" in soru and "itrf96" in soru:
            cevap = "ED50 ↔ ITRF96 dönüşümü 7 parametreyle yapılır. Türkiye için örnek: TX=-87, TY=-98, TZ=-121."
        elif "alan" in soru and "grad" in soru:
            cevap = "Grad ile açı girip üçgen alanı hesaplayabilirim."
        elif "netcad" in soru:
            cevap = "Netcad gibi değil ama Netcad'e uyumlu koordinat dönüşümü ve dosya çıktısı verebilirim."
        else:
            cevap = "Bu konuda emin değilim. UTM, ED50, ITRF96, grad gibi kelimelerle tekrar sorabilirsin."

    return render_template("index.html", cevap=cevap)

if __name__ == "__main__":
    app.run(debug=True)
