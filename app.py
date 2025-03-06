from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)

# Create the database tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to our AI Marketing Tool!"

@app.route('/campaign', methods=['POST'])
def create_campaign():
    data = request.get_json()
    if not data or 'business' not in data or 'budget' not in data:
        return jsonify({"error": "Missing business or budget"}), 400
    
    # Save to database
    new_campaign = Campaign(business=data['business'], budget=data['budget'])
    db.session.add(new_campaign)
    db.session.commit()
    
    return jsonify({"message": f"Campaign {new_campaign.id} for {data['business']} saved"}), 201

if __name__ == '__main__':
    app.run(debug=True)