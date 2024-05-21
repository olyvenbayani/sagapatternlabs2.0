from flask import Flask, request

app = Flask(__name__)

inventory = {'item1': 100, 'item2': 50}

@app.route('/inventory/decrease', methods=['POST'])
def decrease_inventory():
    request_data = request.json
    order_id = request_data['order_id']
    # Simulate inventory decrease
    inventory['item1'] -= 1
    return '', 204

if __name__ == '__main__':
    app.run(port=5002)
