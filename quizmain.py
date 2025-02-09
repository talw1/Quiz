from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, ValidationError

from utils.models import QuizResponse

from quetionHandler import getQuestionXresponse

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='your_secure_secret_key')

class QuizResponse(BaseModel):
   #question_id: int
    answer: str


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this to a specific domain in production)
    #allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/quizzes/{quiz_id}')
async def get_quiz(request: Request,quiz_id: int):

    myQ = getQuestionXresponse()
    wordid=myQ.get_id()
    request.session['myQ_id'] = wordid
    request.session['test_key'] = 'test_value'
    print("Session myQ_id set to:", request.session['myQ_id'])
    print("session:", request.session)
    print(myQ.id,wordid)
    myQ.print_question()
    return myQ




@app.post("/quizzes/submit/")
async def submit_answer(request: Request):
    test_value = request.session.get('test_key', None)
    print("test_value:",test_value)
    print("session:",request.session)
    try:
        body = await request.json()  # Read JSON
        print("Received body:", body)  # Debugging
        # Explicitly validate with Pydantic
        response = QuizResponse(**body)
        wordid = request.session.get('myQ_id', None)
        print("Parsed response:", response)
        print("wordid from session:", wordid)

        quiz_id = request.session.get('quiz_id', None)
        print("Parsed response:", response)
        print("quiz_id from session:", quiz_id)
        return {"message": "Answer received!", "your_answer": response.answer}
    except ValidationError as e:
        print("Validation Error:", e.json())
        raise HTTPException(status_code=422, detail=e.errors())  # More useful error response
    except Exception as e:
        print("General Error:", str(e))
        raise HTTPException(status_code=400, detail="Invalid request format.")


'''
@app.post("/quizzes/submit/")
async def submit_answer(request: Request, response: QuizResponse):
    print(f"Answer Submitted: {response.answer}")
    wordid = request.session.get('myQ_id', None)
    print("word id:", wordid)
    body = await request.json()  # Read the request body
    print("Request Body:", body)

    # If you want to print headers and other info:
    print("Headers:", request.headers)
    print("Method:", request.method)
    print("URL:", request.url)
    if wordid:
        return {'instance_value': wordid}
    else:
        return {'message': 'No instance found.'}

    print(f"Quiz ID: {quiz_id}, Answer Submitted: {response.answer}")
    return {"quiz_id": quiz_id, "message": "Answer received!", "your_answer": response.answer}
'''

