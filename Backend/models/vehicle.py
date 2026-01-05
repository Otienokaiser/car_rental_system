from . import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)  # seats, fuel, engine details etc.
    price_per_day = db.Column(db.Float, nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    # Store image filenames (4 mandatory images)
    image1 = db.Column(db.String(200), nullable=False)
    image2 = db.Column(db.String(200), nullable=False)
    image3 = db.Column(db.String(200), nullable=False)
    image4 = db.Column(db.String(200), nullable=False)

    rentals = db.relationship('Rental', backref='vehicle', lazy=True)
