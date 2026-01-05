from app import db

class VehicleImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
