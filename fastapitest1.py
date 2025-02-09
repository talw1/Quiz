from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel

from quetionHandler import getQuestionXresponse

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='your_secret_key')

class MyClass(BaseModel):
    value: str

@app.get('/set_instance')
async def set_instance(request: Request):

    my_instance = MyClass(value='Hello, World!')
    myQ = getQuestionXresponse()
    print("myQ.id=",myQ.get_id())
    request.session['my_instance'] = my_instance.dict()
    request.session['myQ_id'] = myQ.get_id()
    return {'message': 'Instance set!'}

@app.get('/get_instance')
async def get_instance(request: Request):

    my_instance = request.session.get('my_instance', None)
    wordid = request.session.get('myQ_id', None)
    print("word id:", wordid)
    if my_instance:
       # return {'instance_value': my_instance['value']}
       return {'word id': wordid}

    else:
        return {'message': 'No instance found.'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)