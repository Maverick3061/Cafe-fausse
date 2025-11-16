from flask import Flask, send_from_directory
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db
from routes import bp  # your API blueprint
import os

# Initialize Flask app with React build as static folder
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
mail = Mail(app)
migrate = Migrate(app, db)
CORS(app)

# Register API blueprint
app.register_blueprint(bp, url_prefix='/api')  # all API routes under /api

# Serve React frontend for root
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Catch-all route for React Router (nested frontend routes)
@app.route('/<path:path>')
def serve_react(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        # For all unmatched routes, return index.html
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True)
