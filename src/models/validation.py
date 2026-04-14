from marshmallow import ValidationError, validates, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src import WorkoutExercises, Exercise, Workout


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True

    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)

    @validates('name')
    def validate_name(self, value: str):
        if not value or not value.strip():
            raise ValidationError('Exercise name cannot be blank.')
        if len(value.strip()) < 3:
            raise ValidationError('Exercise name must be at least 3 characters long.')

    @validates('category')
    def validate_category(self, value: str):
        if not value or not value.strip():
            raise ValidationError('Exercise category cannot be blank.')
        allowed = ['strength', 'cardio', 'flexibility', 'balance']
        if value.lower() not in allowed:
            raise ValidationError(f'Category must be one of: {", ".join(allowed)}.')

    @validates('equipment_needed')
    def validate_equipment_needed(self, value: bool):
        if not isinstance(value, bool):
            raise ValidationError('equipment_needed must be a boolean (true or false).')


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True

    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration = fields.Int(required=True)
    notes = fields.Str(required=True)
    workout_exercises = fields.List(
        fields.Nested(lambda: WorkoutExercisesSchema(), dump_only=True),
        dump_only=True
    )

    @validates('duration')
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError('Duration must be greater than 0.')

    @validates('notes')
    def validate_notes(self, value):
        if not value or not value.strip():
            raise ValidationError('Notes cannot be blank.')


class WorkoutExercisesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercises
        load_instance = True

    id = fields.Int(dump_only=True)
    workout_id = fields.Int(load_only=True, required=True)
    exercise_id = fields.Int(load_only=True, required=True)
    reps = fields.Int(required=True)
    sets = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)
    exercise = fields.Nested(ExerciseSchema, dump_only=True)

    @validates('reps')
    def validate_reps(self, value):
        if value <= 0:
            raise ValidationError('Reps must be greater than 0.')

    @validates('sets')
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError('Sets must be greater than 0.')

    @validates('duration_seconds')
    def validate_duration_seconds(self, value):
        if value <= 0:
            raise ValidationError('Duration in seconds must be greater than 0.')


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExercisesSchema()
workout_exercises_schema = WorkoutExercisesSchema(many=True)