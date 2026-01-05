from flask import Blueprint, jsonify, send_from_directory
from models.vehicle import Vehicle  # Your vehicle model with image URLs
import os

main = Blueprint('main', __name__)

# API endpoint to get vehicles
@main.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()

    vehicle_list = []
    for v in vehicles:
        vehicle_list.append({
            "id": v.id,
            "name": v.name,
            "description": v.description,
            "price": f"KES {v.price_per_day}/day or KES {v.price_per_month}/month",
            "images": [img.url for img in v.images]  # assuming you have a relationship to images
        })

    return jsonify(vehicle_list)

# Serve the landing page (index.html)
@main.route('/')
def index():
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Frontend'))
    return send_from_directory(frontend_dir, 'index.html')

# Serve other frontend static files (css, js, images, etc.)
@main.route('/<path:path>')
def static_proxy(path):
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Frontend'))
    return send_from_directory(frontend_dir, path)
