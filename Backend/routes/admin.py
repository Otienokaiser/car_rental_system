from flask import Blueprint, request, jsonify
from models import db
from models.vehicle import Vehicle

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    required_fields = ['name', 'description', 'price_per_day', 'price_per_month',
                       'image1', 'image2', 'image3', 'image4']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing vehicle fields'}), 400

    # Check image file sizes and validation should be done on frontend ideally
    # Here just accept the image filenames (assume upload done separately)
    vehicle = Vehicle(
        name=data['name'],
        description=data['description'],
        price_per_day=float(data['price_per_day']),
        price_per_month=float(data['price_per_month']),
        image1=data['image1'],
        image2=data['image2'],
        image3=data['image3'],
        image4=data['image4'],
        is_available=True
    )
    db.session.add(vehicle)
    db.session.commit()

    return jsonify({'message': 'Vehicle added successfully', 'vehicle_id': vehicle.id}), 201
