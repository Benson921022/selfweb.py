from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# 讓 Vercel 認得的 entry point（handler）
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
