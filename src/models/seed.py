from app import app
from faker import Faker
from src import db, Exercise, Workout, WorkoutExercises
from random import randint, choice

fake = Faker()


def clear_tables():
    print("Clearing old data...")
    db.session.query(WorkoutExercises).delete()
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()
    db.session.commit()


def create_exercise():
    print("Seeding exercises...")
    try:
        for _ in range(10):
            exercise = Exercise(
                name=fake.unique.word(),
                category=fake.word(),
                equipment_needed=fake.boolean()
            )
            db.session.add(exercise)
        db.session.commit()
        print("Seed exercise executed")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred seeding exercises: {str(e)}")


def seed_workouts():
    print("Seeding workouts....")
    try:
        for _ in range(20):
            workout = Workout(
                date=fake.date_this_month(),
                duration=randint(15, 120),
                notes=fake.sentence()
            )
            db.session.add(workout)
        db.session.commit()
        print("Seed workout executed")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred seeding workouts: {str(e)}")


def seed_workout_exercises():
    print("Seeding workout exercises....")
    try:

        workouts = Workout.query.all()
        exercises = Exercise.query.all()


        existing_pairs = set()

        for _ in range(15):
            random_workout = choice(workouts)
            random_exercise = choice(exercises)
            pair = (random_workout.id, random_exercise.id)

            if pair not in existing_pairs:
                workout_exercise = WorkoutExercises(
                    workout_id=random_workout.id,
                    exercise_id=random_exercise.id,
                    reps=randint(5, 20),
                    sets=randint(1, 5),
                    duration_seconds=randint(60, 300)
                )
                db.session.add(workout_exercise)
                existing_pairs.add(pair)

        db.session.commit()
        print("Seed workout exercises executed")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred seeding workout exercises: {str(e)}")


if __name__ == '__main__':
    with app.app_context():
        clear_tables()
        create_exercise()
        seed_workouts()
        seed_workout_exercises()