from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db
from models.vehicle import Vehicle
from models.rental import Rental
from models.user import User

client_bp = Blueprint('client', __name__)

@client_bp.route('/vehicles', methods=['GET'])
def get_available_vehicles():
    vehicles = Vehicle.query.filter_by(is_available=True).all()
    result = []
    for v in vehicles:
        result.append({
            'id': v.id,
            'name': v.name,
            'description': v.description,
            'price_per_day': v.price_per_day,
            'price_per_month': v.price_per_month,
            'images': [v.image1, v.image2, v.image3, v.image4]
        })
    return jsonify(result), 200

@client_bp.route('/rent', methods=['POST'])
def rent_vehicle():
    data = request.json
    required_fields = ['user_id', 'vehicle_id', 'start_date', 'end_date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    vehicle = Vehicle.query.get(data['vehicle_id'])
    if not vehicle or not vehicle.is_available:
        return jsonify({'error': 'Vehicle not available'}), 400

    # Check dates validity
    try:
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d").date()
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    if start_date > end_date:
        return jsonify({'error': 'Start date must be before end date'}), 400

    # Calculate price (simplified logic)
    days = (end_date - start_date).days + 1
    if days >= 30:
        price = vehicle.price_per_month * (days // 30)
        price += vehicle.price_per_day * (days % 30)
    else:
        price = vehicle.price_per_day * days

    rental = Rental(
        user_id=data['user_id'],
        vehicle_id=vehicle.id,
        start_date=start_date,
        end_date=end_date,
        total_price=price
    )
    vehicle.is_available = False  # mark as rented
    db.session.add(rental)
    db.session.commit()

    return jsonify({'message': 'Vehicle rented successfully', 'total_price': price}), 201

@client_bp.route('/return', methods=['POST'])
def return_vehicle():
    data = request.json
    if not data or not data.get('rental_id'):
        return jsonify({'error': 'Rental ID required'}), 400

    rental = Rental.query.get(data['rental_id'])
    if not rental:
        return jsonify({'error': 'Rental not found'}), 404

    vehicle = Vehicle.query.get(rental.vehicle_id)
    vehicle.is_available = True
    db.session.delete(rental)
    db.session.commit()

    return jsonify({'message': 'Vehicle returned successfully'}), 200
