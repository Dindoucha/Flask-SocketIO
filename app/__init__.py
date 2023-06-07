from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import TestingConfig
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
jwt = JWTManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(TestingConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, cors_allowed_origins=["http://localhost:3000"])

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}},
        headers={'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Allow-Origin': 'http://localhost:3000'},
        supports_credentials=True)

    jwt.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    from .routes import routes_bp 
    # Add the rest of your code here
    app.register_blueprint(routes_bp)

    return app