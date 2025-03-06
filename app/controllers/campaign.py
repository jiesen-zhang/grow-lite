from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.campaign import Campaign

campaign_bp = Blueprint('campaign', __name__)

@campaign_bp.route('/')
def home():
    return "Welcome to our AI Marketing Tool!"

@campaign_bp.route('/campaign', methods=['POST'])
def create_campaign():
    data = request.get_json()
    if not data or 'business' not in data or 'budget' not in data:
        return jsonify({"error": "Missing business or budget"}), 400
    
    new_campaign = Campaign(business=data['business'], budget=data['budget'])
    db.session.add(new_campaign)
    db.session.commit()
    
    return jsonify({"message": f"Campaign {new_campaign.id} for {data['business']} saved"}), 201