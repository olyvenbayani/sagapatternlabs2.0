from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saga', methods=['POST'])
def start_saga():
    # Example implementation
    return jsonify({'message': 'Saga started'}), 200

if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0')