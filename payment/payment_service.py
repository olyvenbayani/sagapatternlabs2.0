from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

payments = {}

@app.route('/payments', methods=['POST'])
def process_payment():
    payment = request.json
    payment_id = len(payments) + 1
    payment['id'] = payment_id
    payments[payment_id] = payment
    # Simulate payment processing
    payment['status'] = 'completed'
    requests.put(f'http://localhost:5000/orders/{payment["id"]}/status', json={'status': 'completed'})
    requests.post('http://localhost:5002/inventory/decrease', json={'order_id': payment['id']})
    return jsonify(payment), 201

if __name__ == '__main__':
    app.run(port=5001)
