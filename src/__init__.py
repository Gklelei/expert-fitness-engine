from src.models.config import db,ma
from src.models.models import Exercise,Workout,WorkoutExercises
from src.models.validation import exercise_schema,exercises_schema,workout_schema,workout_exercises_schema,workouts_schema,workout_exercise_schema
from src.routes.routes import workout_bp,exercise_bp