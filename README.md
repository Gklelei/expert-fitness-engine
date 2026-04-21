# Expert Fitness Engine

A RESTful API for fitness tracking built with Flask, SQLAlchemy, and SQLite. This application allows you to manage exercises, workouts, and track your fitness progress.

## Tech Stack

- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Package Manager**: UV
- **Python Version**: 3.12

## Requirements

- Python 3.12 (you can change the version in `pyproject.toml` if needed)
- UV package manager

> **Note**: This guide is written for Ubuntu users. Commands may vary on different operating systems.

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:Gklelei/expert-fitness-engine.git
cd expert-fitness-engine
```

### 2. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Seed Initial Data (Optional)

To populate the database with initial sample data:

```bash
export FLASK_APP=app.py
python -m src.models.seed
```

This will create sample exercises and workouts to help you get started quickly.

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5555` in debug mode.

> **Note**: No authentication is required for any endpoints.

## API Endpoints

### Exercises

#### Create an Exercise

Create a new exercise in the database.

- **Method**: `POST`
- **URL**: `/exercises`
- **Body** (JSON):
```json
{
  "name": "biceps",
  "category": "strength",
  "equipment_needed": true
}
```
- **Success Response**:
```json
{
  "message": "Exercise created successfully"
}
```

---

#### Get All Exercises

Retrieve a list of all exercises.

- **Method**: `GET`
- **URL**: `/exercises`
- **Success Response**:
```json
[
  {
    "id": 1,
    "name": "phone",
    "category": "quality",
    "equipment_needed": true,
    "workouts": [
      {
        "id": 2,
        "sets": 2,
        "reps": 14,
        "duration_seconds": 164
      }
    ]
  }
]
```

---

#### Get Exercise by ID

Retrieve a specific exercise with its associated workout exercises.

- **Method**: `GET`
- **URL**: `/exercises/<id>`
- **Success Response**:
```json
{
  "id": 7,
  "name": "realize",
  "category": "indeed",
  "equipment_needed": true,
  "workouts": [
    {
      "id": 14,
      "sets": 5,
      "reps": 18,
      "duration_seconds": 289
    },
    {
      "id": 9,
      "sets": 3,
      "reps": 20,
      "duration_seconds": 212
    },
    {
      "id": 4,
      "sets": 3,
      "reps": 17,
      "duration_seconds": 278
    }
  ]
}
```

---

#### Delete an Exercise

Delete an exercise from the database.

- **Method**: `DELETE`
- **URL**: `/exercises/<id>`
- **Success Response**:
```json
{
  "message": "Exercise has been deleted"
}
```

---

### Workouts

#### Create a Workout

Create a new workout session.

- **Method**: `POST`
- **URL**: `/workouts`
- **Body** (JSON):
```json
{
  "date": "2026-04-15",
  "duration": 50,
  "notes": "Workout notes"
}
```
- **Success Response**:
```json
{
  "message": "Workout has been created"
}
```

---

#### Get All Workouts

Retrieve a list of all workouts.

- **Method**: `GET`
- **URL**: `/workouts`
- **Success Response**:
```json
[
  {
    "id": 2,
    "date": "2026-04-04",
    "duration": 26,
    "notes": "Chair opportunity care PM.",
    "workout_exercises": [
      {
        "id": 3,
        "sets": 1,
        "reps": 8,
        "duration_seconds": 131,
        "exercise": {
          "id": 10,
          "name": "indicate",
          "category": "instead",
          "equipment_needed": false,
          "workouts": [
            {
              "id": 3,
              "sets": 1,
              "reps": 8,
              "duration_seconds": 131
            }
          ]
        }
      }
    ]
  }
]
```

---

#### Get Workout by ID

Retrieve a specific workout with all associated exercises.

- **Method**: `GET`
- **URL**: `/workouts/<workout_id>`
- **Success Response**:
```json
{
  "id": 10,
  "date": "2026-04-07",
  "duration": 79,
  "notes": "House somebody newspaper class sense grow large.",
  "workout_exercises": [
    {
      "id": 7,
      "sets": 5,
      "reps": 12,
      "duration_seconds": 229,
      "exercise": {
        "id": 2,
        "name": "necessary",
        "category": "strategy",
        "equipment_needed": true,
        "workouts": [
          {
            "id": 4,
            "sets": 2,
            "reps": 5,
            "duration_seconds": 262
          },
          {
            "id": 7,
            "sets": 5,
            "reps": 12,
            "duration_seconds": 229
          }
        ]
      }
    }
  ]
}
```

---

#### Delete a Workout

Delete a workout from the database.

- **Method**: `DELETE`
- **URL**: `/workouts/<id>`
- **Success Response**:
```json
{
  "message": "Workout has been deleted"
}
```

---

### Workout Exercises

#### Add Exercise to Workout

Link an exercise to a specific workout with performance details.

- **Method**: `POST`
- **URL**: `/workouts/<workout_id>/exercise/<exercise_id>/workout_exercises`
- **Body** (JSON):
```json
{
  "reps": 5,
  "sets": 2,
  "duration_seconds": 300
}
```
- **Success Response**:
```json
{
  "message": "Workout Exercise Created successfully"
}
```
