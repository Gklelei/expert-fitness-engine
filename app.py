from flask import Flask
from src import db,ma
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True , port=5555)