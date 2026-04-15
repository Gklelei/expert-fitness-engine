from marshmallow import ValidationError
from src import db,workout_exercise_schema,WorkoutExercises
from flask import jsonify as res_json , request as req

def create_workout_exercises(workout_id,exercise_id):
    if not workout_id or not exercise_id:
        return res_json({"message":"Workout ID or Exercise ID is and is  required."}),400

    data = req.get_json()

    data['workout_id'] = workout_id
    data['exercise_id'] = exercise_id

    try:
        parsed_data = workout_exercise_schema.load(data, session=db.session)
    except ValidationError as e:
        return res_json(e.messages), 422

    try:
        db.session.add(parsed_data)
        db.session.commit()

        return res_json({"message":"Workout Exercise Created successfully"}),201

    except Exception as e:
        print(str(e))
        return res_json({"message":"Internal server error"})