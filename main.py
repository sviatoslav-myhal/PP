from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/hello-world-5")
def hello_world():
   return "<p>Hello World 5</p>"

@app.route("/api/v1/hello-world")
def hello_world2():
   return "<p>Hello World</p>"

# venv\Scripts\activate
# waitress-serve --host 127.0.0.1 --port=5000 --call "main:create_app"
# /api/v1/hello-world-15+
# /api/v1/hello-world

# curl -v -XGET http://localhost:5000/api/v1/hello-wor
# ld-5