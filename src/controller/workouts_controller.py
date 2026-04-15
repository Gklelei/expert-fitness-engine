from src import Workout,workouts_schema,workout_schema,db
from flask import jsonify as res_json, request as req
from marshmallow import ValidationError


def create_workouts():
    data = req.get_json()

    if not data:
        return res_json({"message": "Request body cannot be empty"}),400

    try:
        parsed_data = workout_schema.load(data,session=db.session)
    except ValidationError as e:
        return res_json(e.messages),422

    try:
        db.session.add(parsed_data)
        db.session.commit()

        return res_json({"message":"Workout has been created"}),201
    except Exception as e:
        db.session.rollback()
        print(e)
        return res_json({"message":"Internal server error"}),500


def get_workouts():
    try:
        workouts = db.session.query(Workout).all()

        if not workouts or len(workouts) == 0:
            return res_json({"message": "No workouts found"}),400

        return res_json(workouts_schema.dump(workouts)),200

    except Exception as e:
        print(str(e))
        return  res_json({"message":"Internal server error"}),500

def get_workout(id):
    if not id:
        return  res_json({"message": "Workout id is required"}),400
    try:
        workout = db.session.query(Workout).filter_by(id=id).one_or_none()

        if not workout:
            return  res_json({"message":f"Workout with id: {id} not found"})

        return res_json(workout_schema.dump(workout)),200
    except Exception as e:
        print(str(e))
        return res_json({"message":"Internal server error"}),500

def delete_workout(id):
    if not id:
        return  res_json({"message": "Workout id is required"}),400

    try:
        existing_workout = db.session.query(Workout).filter_by(id=id).one_or_none()

        if not existing_workout:
            return res_json({"message": f"Workout with id: {id} not found"})

        db.session.delete(existing_workout)
        db.session.commit()

        return res_json({"message":"Workout has been deleted"}),200
    except Exception as e:
        print(str(e))
        return res_json({"message":"Internal server error"}),500
