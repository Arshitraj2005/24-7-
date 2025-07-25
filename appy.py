from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Streaming is active"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
