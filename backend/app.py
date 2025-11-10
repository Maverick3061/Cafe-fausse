from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
mail = Mail(app)
migrate = Migrate(app, db)
CORS(app)

# Register Blueprint
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
