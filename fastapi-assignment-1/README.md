# Student Management API

This is a simple RESTful API built with FastAPI for managing a list of students.

## Setup Instructions

1. Install FastAPI: `pip install fastapi`
2. Install Uvicorn (an ASGI server): `pip install uvicorn`
3. Run the server: `uvicorn asgnmnt1.main:app --reload --port 8080`
4. Open http://localhost:8080/docs in your browser to view interactive API documentation.
You can test the endpoints directly from the browser.


## API Overview

- `GET /students`: Retrieve all students.
- `GET /students/{student_id}`: Retrieve specific student details.
- `POST /students`: Add a new student.
- `PUT /students/{student_id}`: Update a student's details.
- `DELETE /students/{student_id}`: Delete a student.

Each student object should have:
- `id`: The student's unique ID.
- `name`: The student's name.
- `age`: The student's age.
- `grade`: The student's grade/class.
