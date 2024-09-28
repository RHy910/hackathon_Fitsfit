from flask import Flask
from flask import render_template
from config import Config
from routes import main as main_routes
from models import db


app = Flask(__name__)
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)