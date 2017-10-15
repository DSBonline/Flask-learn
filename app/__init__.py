from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main as main_blueprints

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(main_blueprints)
