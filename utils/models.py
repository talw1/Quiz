from pydantic import BaseModel
from typing import List, Dict


class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_index: int

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_question(self) -> str:
        return self.question

    def set_question(self, question: str):
        self.question = question

    def get_options(self) -> List[str]:
        return self.options

    def set_options(self, options: List[str]):
        self.options = options

    def get_correct_index(self) -> int:
        return self.correct_index

    def set_correct_index(self, correct_index: int):
        self.correct_index = correct_index

    def print_question(self):
        print(f"Question ID: {self.id}")
        print(f"Question: {self.question}")
        print(f"Options: {', '.join(self.options)}")
        print(f"Correct Index: {self.correct_index}")

class QuizResponse(BaseModel):
    quiz_id: int
    answer: str