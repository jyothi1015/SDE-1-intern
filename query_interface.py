from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query_logs():
    query_params = request.args.to_dict()

    if not query_params:
        return jsonify({"error": "No query parameters provided"}), 400

    filtered_logs = filter_logs(query_params)
    return jsonify({"logs": filtered_logs})

def filter_logs(query_params):
    return [log for log in logs if all(log.get(key) == value for key, value in query_params.items())]

if __name__ == '__main__':
    app.run(port=3001)
