from flask import Flask, request, jsonify

app = Flask(__name__)
logs = []

@app.route('/ingest', methods=['POST'])
def ingest_log():
    data = request.get_json()

    if 'message' not in data or 'timestamp' not in data:
        return jsonify({"error": "Invalid log format"}), 400

    logs.append(data)
    return jsonify({"message": "Log ingested successfully"}), 201

if __name__ == '__main__':
    app.run(port=3000)
