import  random
from utils.vocDBactions import selectwords
from utils.models import Question

def getQuestionXresponse():
    print("****Start run_quiz4response *******")
    #def run_quiz4response(words, num_questions=3):
    # Shuffle the list of words

    words = selectwords()


    random_element = random.choice(words)

    english=random_element[1]
    id=random_element[0]
    correct_hebrew = random_element[2]

        # Generate 3 incorrect options
        #incorrect_options = random.sample([hebrew for _, hebrew in words if hebrew != correct_hebrew], 3)

    filtered_words = [word[2] for word in words if word[2] != correct_hebrew]
        # Pick 3 random words from the filtered list
    incorrect_options = random.sample(filtered_words, 3)

        # Combine correct option with incorrect options and shuffle them
    options = incorrect_options + [correct_hebrew]
    random.shuffle(options)
    index = next((i for i, val in enumerate(options) if val == correct_hebrew), -1)
    q = Question(id=id,question=english,options=options,correct_index=index)

    # Ask the user for the translation
    print(f"What is the Hebrew translation for '{english}'?")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    print("****End run_quiz4response *******")
    return q