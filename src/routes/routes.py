from flask import Blueprint

#Blueprints
workout_bp = Blueprint('workout', __name__)
exercise_bp = Blueprint('exercise', __name__)

# Workout
workout_bp.route("/", methods=["GET"])
workout_bp.route("/", methods=["POST"])
workout_bp.route("/<int:id>", methods=["GET"])
workout_bp.route("/<int:id>", methods=["POST"])

# Exercise
exercise_bp .route("/", methods=["GET"])
exercise_bp .route("/", methods=["POST"])
exercise_bp .route("/<int:id>", methods=["GET"])
exercise_bp .route("/<int:id>", methods=["POST"])

# workout_exercises
workout_bp.route('/<int:workout_id>/exercise/<int:exercise_id>/workout_exercises', methods=["GET"])