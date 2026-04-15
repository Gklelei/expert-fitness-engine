from flask import Blueprint
from src.controller.exercises_controller import create_exercise,get_all_exercises,get_exercise,delete_exercise

#Blueprints
workout_bp = Blueprint('workout', __name__)
exercise_bp = Blueprint('exercise', __name__)

# Workout
workout_bp.route("/", methods=["GET"])
workout_bp.route("/", methods=["POST"])
workout_bp.route("/<int:id>", methods=["GET"])
workout_bp.route("/<int:id>", methods=["DELETE"])

# Exercise
exercise_bp .route("/", methods=["GET"])(get_all_exercises)
exercise_bp .route("/", methods=["POST"])(create_exercise)
exercise_bp .route("/<int:id>", methods=["GET"])(get_exercise)
exercise_bp .route("/<int:id>", methods=["DELETE"])(delete_exercise)

# workout_exercises
workout_bp.route('/<int:workout_id>/exercise/<int:exercise_id>/workout_exercises', methods=["GET"])