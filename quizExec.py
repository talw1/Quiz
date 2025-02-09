import random

from quetionHandler import getQuestionXresponse
from utils.vocDBactions import cursor, conn, selectwords


def run_quiz(words, num_questions=5):
    # Shuffle the list of words
    # List of words in English and their translations in Hebrew

    random.shuffle(words)

    score = 0

    for i in range(num_questions):
        english, hebrew = words[i]
        # Ask the user for the translation
        answer = input(f"What is the Hebrew translation for '{english}'? ")

        if answer.strip() == hebrew:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{hebrew}'.")

    print(f"Quiz finished! Your score is {score}/{num_questions}.")


def run_quiz4response(num_questions=3):
    print("****Start run_quiz4response *******")
    #def run_quiz4response(words, num_questions=3):
    # Shuffle the list of words
    words = selectwords()
    score = 0

    for i in range(num_questions):
        random_element = random.choice(words)
        print(random_element)
        print(random_element[1])
        english=random_element[1]
        correct_hebrew = random_element[2]

        # Generate 3 incorrect options
        #incorrect_options = random.sample([hebrew for _, hebrew in words if hebrew != correct_hebrew], 3)

        filtered_words = [word[2] for word in words if word[2] != correct_hebrew]
        # Pick 3 random words from the filtered list
        incorrect_options = random.sample(filtered_words, 3)

        print(incorrect_options)
        # Combine correct option with incorrect options and shuffle them
        options = incorrect_options + [correct_hebrew]
        random.shuffle(options)

        # Ask the user for the translation
        print(f"What is the Hebrew translation for '{english}'?")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        answer = input("Choose the correct option (1-4): ")

        if options[int(answer) - 1] == correct_hebrew:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{correct_hebrew}'.")

    print(f"Quiz finished! Your score is {score}/{num_questions}.")

def checkResponseCorrectness(user_answer,word):
    is_correct = user_answer.lower() == word[2].lower()
    cursor.execute('''
      INSERT INTO QuizResults (word_id, user_answer, is_correct)
      VALUES (?, ?, ?)
      ''', (word[0], user_answer, is_correct))
    conn.commit()
    print("Correct!" if is_correct else f"Wrong! The correct translation is {word[2]}.")


# Function to quiz the user
def quiz_user():

    cursor.execute('SELECT * FROM Words ORDER BY RANDOM() LIMIT 1')
    word = cursor.fetchone()
    print(f"Translate the word: {word[1]} ,  {word[2]}")
    user_answer = input("Your answer: ")
    is_correct = user_answer.lower() == word[2].lower()
    cursor.execute('''
    INSERT INTO QuizResults (word_id, user_answer, is_correct)
    VALUES (?, ?, ?)
    ''', (word[0], user_answer, is_correct))
    conn.commit()
    print("Correct!" if is_correct else f"Wrong! The correct translation is {word[2]}.")


def main_menu():
    print("Welcome to the Quiz Application!")
    print("1. Start Quiz")
    print("2. View Scores")
    print("3. Settings")
    print("4. Logout")
    choice = input("Enter your choice: ")
    if choice == '1':
        start_quiz()
    elif choice == '2':
        view_scores()
    elif choice == '3':
        settings()
    elif choice == '4':
        logout()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_quiz():
    print("Starting the quiz...")
    quiz_user()
    # Implement quiz logic here

def view_scores():
    print("Viewing scores...")
    # Implement score viewing logic here

def settings():
    print("Settings...")
    # Implement settings logic here

def logout():
    print("Logging out...")
    # Implement logout logic here

# Example usage


def selectwords1():
    print("Start selectwords1:  ")
    cursor.execute("SELECT * FROM words")
    rows = cursor.fetchall()  # Fetch all results
    return  rows
#main_menu()
def testquiz1(num_questions=3):
    print("****Start testquiz1 *******")
    #def run_quiz4response(words, num_questions=3):
    # Shuffle the list of words
    words = selectwords1()

    score = 0
def printH():
    print("printH Hello quizExec")
    q=getQuestionXresponse()
    print(q.question)
    return q
#run_quiz(name_value_pairs,2)
#run_quiz4response(2)