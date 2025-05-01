from flask import Flask
from flask_migrate import Migrate
from database_init import db
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('ADDRESS_DB')}/{os.getenv('NAME_DB')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)
    
    from routes.home import home_bp
    from routes.survey import survey_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(survey_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
