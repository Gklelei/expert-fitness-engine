from flask import Flask
from src import db,ma
from flask_migrate import Migrate
from src import exercise_bp,workout_bp
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(exercise_bp, url_prefix='/exercises')
app.register_blueprint(workout_bp, url_prefix='/workouts')

db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True , port=5555)