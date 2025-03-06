from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our AI Marketing Tool!"

@app.route('/campaign', methods=['POST'])
def create_campaign():
    data = request.get_json()  # Expect JSON input like {"business": "coffee shop", "budget": 200}
    if not data or 'business' not in data or 'budget' not in data:
        return jsonify({"error": "Missing business or budget"}), 400
    return jsonify({"message": f"Campaign for {data['business']} with ${data['budget']} received"}), 200

if __name__ == '__main__':
    app.run(debug=True)