from flask import Blueprint
from src.controller.exercises_controller import create_exercise,get_all_exercises,get_exercise,delete_exercise
from src.controller.workouts_controller import create_workouts,get_workouts,get_workout,delete_workout
#Blueprints
workout_bp = Blueprint('workout', __name__)
exercise_bp = Blueprint('exercise', __name__)

# Workout
workout_bp.route("/", methods=["GET"])(get_workouts)
workout_bp.route("/", methods=["POST"])(create_workouts)
workout_bp.route("/<int:id>", methods=["GET"])(get_workout)
workout_bp.route("/<int:id>", methods=["DELETE"])(delete_workout)

# Exercise
exercise_bp .route("/", methods=["GET"])(get_all_exercises)
exercise_bp .route("/", methods=["POST"])(create_exercise)
exercise_bp .route("/<int:id>", methods=["GET"])(get_exercise)
exercise_bp .route("/<int:id>", methods=["DELETE"])(delete_exercise)

# workout_exercises
workout_bp.route('/<int:workout_id>/exercise/<int:exercise_id>/workout_exercises', methods=["GET"])