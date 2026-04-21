from src import Exercise,db,exercise_schema,exercises_schema
from flask import jsonify as res_json, request as req
from marshmallow import ValidationError

def create_exercise():
    data = req.get_json()

    try:
        parsed_data = exercise_schema.load(data, session=db.session)
    except ValidationError as e:
        return res_json(e.messages),422

    try:
        name = parsed_data.name.lower()

        existing_exercise = db.session.query(Exercise).filter_by(name=name).one_or_none()

        if existing_exercise:
            return res_json({'message':'Exercise already exists'}),409

        parsed_data.name = name

        db.session.add(parsed_data)
        db.session.commit()

        return res_json({'message':'Exercise created successfully'}),201
    except ValidationError as e:
        db.session.rollback()
        print(str(e))
        return res_json({"message":"Internal Server Error"}),500

def get_all_exercises():
    try:
        exercise = db.session.query(Exercise).all()

        if not exercise or len(exercise) == 0:
            return res_json({'message':'Exercises not found'}),404


        return res_json(exercises_schema.dump(exercise)),200

    except Exception as e:
        print(str(e))
        return res_json({"message":"Internal Server Error"}),500


def get_exercise(id):
     if not id:
         return res_json({"message":"Exercise id is required"}),400

     try:
         exercise = db.session.query(Exercise).filter_by(id=id).one_or_none()

         if not exercise:
             return res_json({"message":f"Exercise with id {id} not found"}),404

         return res_json(exercise_schema.dump(exercise)),200
     except Exception as e:
         print(str(e))
         return res_json({"message":"Internal Server Error"}),500

def delete_exercise(id):
    if not id:
        return res_json({"message": "Exercise id is required"}), 400
    try:
        existing_exercise = db.session.query(Exercise).filter_by(id=id).one_or_none()

        if not existing_exercise:
            return res_json({"message":"Exercise does not exist"}),404

        db.session.delete(existing_exercise)

        db.session.commit()

        return res_json({"message":"Exercise has been deleted"}),200
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return res_json({"message":"Internal server error"}),500