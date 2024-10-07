from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route('/')
def hello():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})

@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if item:
        items.append(item)
        return jsonify({"message": "Item added successfully"}), 201
    return jsonify({"error": "Invalid item"}), 400

if __name__ == '__main__':
    app.run(debug=True)