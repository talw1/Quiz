from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict

from quizExec import run_quiz4response
#from Quiz.vocDBactions import selectwords

app = FastAPI()

# Mock database
quizzes = []
users = {}

### --- Authentication Models --- ###
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

### --- Quiz Models --- ###
class Question(BaseModel):
    question: str
    options: List[str]
    correct_index: int

class Quiz(BaseModel):
    title: str
    questions: List[Question]

class QuizResponse(BaseModel):
    answers: List[int]  # List of selected answer indexes

### --- Authentication Endpoints --- ###
@app.post("/register")
def register(user: UserRegister):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.username] = user.password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: UserLogin):
    if users.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "token": f"fake_token_{user.username}"}

### --- Quiz Endpoints --- ###
@app.get("/quizzes", response_model=List[Quiz])
def get_quizzes():
    print('t')
    return quizzes

@app.post("/quizzes")
def create_quiz(quiz: Quiz):
    print('post t')
    quizzes.append(quiz)
    return {"message": "Quiz added"}

@app.get("/quizzes/{quiz_id}")
def get_quiz(quiz_id: int):
    print("-------1---Quiz-----------")
    run_quiz4response(2)
    if quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quizzes[quiz_id]

@app.post("/quizzes/{quiz_id}/submit")
def submit_quiz(quiz_id: int, response: QuizResponse):
    if quiz_id >= len(quizzes):
        raise HTTPException(status_code=404, detail="Quiz not found")

    quiz = quizzes[quiz_id]
    score = sum(
        1 for i, answer in enumerate(response.answers)
        if i < len(quiz.questions) and quiz.questions[i].correct_index == answer
    )

    return {"score": score, "total": len(quiz.questions)}

### --- Run Server --- ###
# Run this command in terminal to start the server:
# uvicorn main:app --reload