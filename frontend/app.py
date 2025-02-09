from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample quiz questions
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"]
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"]
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Shakespeare", "Hemingway", "Tolkien", "Austen"]
    }
]

@app.route('/quiz', methods=['GET'])
def get_quiz():
    quiz = random.choice(quiz_data)
    print (quiz)
    return jsonify(quiz)

if __name__ == '__main__':
    app.run(debug=True)