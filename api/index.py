from flask import Flask, render_template

# 正確格式：定義 app，Vercel 會自動辨識這個變數
app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")
