from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    order_id = len(orders) + 1
    order['id'] = order_id
    order['status'] = 'pending'
    orders[order_id] = order
    # Send order created event
    requests.post('http://localhost:5001/payments', json=order)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    status = request.json['status']
    if order_id in orders:
        orders[order_id]['status'] = status
        return '', 204
    return 'Order not found', 404

if __name__ == '__main__':
    app.run(port=5000)
