from flask import Flask, request, jsonify

app = Flask(__name__)

data = {"ecg": 0, "ppg": 0}

@app.route("/send", methods=["POST"])
def send():
    global data
    data = request.json
    return "OK"

@app.route("/get", methods=["GET"])
def get():
    return jsonify(data)

@app.route("/")
def home():
    return "Server is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
