from flask import Flask,render_template #flask frameworku icindeki flask sınıfını dahil ediyoruz


app = Flask(__name__)
@app.route("/")
def index():
    articles=[
        {"id":1 ,"title":"deneme1","content":"deneme1 icerik"},
        {"id":2 ,"title":"deneme2","content":"deneme2 icerik"},
        {"id":3 ,"title":"deneme3","content":"deneme1 icerik"}




    ]
    return render_template("index.html" ,articles= articles)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/article/<string:id>")  #flask dinamik url güzelce arastir
def detail(id):
    return "article id " + id


if __name__ == "__main__":
    app.run(debug=True) #web sunucumuz hata mesajlarımızı göstericek
