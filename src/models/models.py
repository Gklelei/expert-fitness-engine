from src import db

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_exercises = db.relationship('WorkoutExercises', back_populates='exercise')
    workouts = db.relationship('Workouts', back_populates='exercise',viewonly=True)


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    workout_exercises = db.relationship('WorkOutExercises', back_populates='workout')
    exercise =db.relationship('Exercise', back_populates='workout_exercises', viewonly=True)


class WorkoutExercises(db.Model):
    __tablename__ = "workouts_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')