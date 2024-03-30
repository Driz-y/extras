from fastapi import FastAPI
import uvicorn

app = FastAPI()


students = {}


from typing import Dict

@app.get("/")
def helloWorld():
    return{"Assignment" : "1"}

@app.get("/students")
def get_all_students() -> Dict[str, Dict]:
    return students

@app.get("/students/{student_id}")
def get_student(student_id: str) -> Dict:
    return students.get(student_id, {})

@app.post("/students")
def create_student(student_id: str, name: str, age: int, grade: str) -> Dict:
    student = {"name": name, "age": age, "grade": grade}
    students[student_id] = student
    return student

@app.put("/students/{student_id}")
def update_student(student_id: str, name: str, age: int, grade: str) -> Dict:
    if student_id in students:
        students[student_id] = {"name": name, "age": age, "grade": grade}
        return students[student_id]
    return {}

@app.delete("/students/{student_id}")
def delete_student(student_id: str) -> Dict:
    if student_id in students:
        return students.pop(student_id)
    return {}


