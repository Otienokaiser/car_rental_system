from flask import Flask
from models import db
from werkzeug.security import generate_password_hash

def create_default_admin():
    from models.user import User

    admin_email = "admin@local.com"

    if not User.query.filter_by(email=admin_email).first():
        admin = User(
            name="Super Admin",
            email=admin_email,
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Default admin created")

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-secret-key"

    db.init_app(app)

    # Import and register blueprints
    from routes import main, auth, client, admin
    app.register_blueprint(main)        # main is already the blueprint object
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')
    app.register_blueprint(client.client_bp, url_prefix='/client')
    app.register_blueprint(admin.admin_bp, url_prefix='/admin')

    with app.app_context():
        db.create_all()       # Create tables if not existing
        create_default_admin() # Insert default admin if not present

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
