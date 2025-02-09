
from utils.DBConnection import cursor,conn
from manageVocFiles import read_file_to_name_value_list


# select from table
# -------------------------#

def selectQueryusers():
    print("Start selectQueryusers:  ")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()  # Fetch all results
    for row in rows:
        print(row)


def selectwords():
    print("Start selectwords:  ")
    cursor.execute("SELECT * FROM words")
    rows = cursor.fetchall()  # Fetch all results
    return  rows


# Function to add a word
def add_word(englishword, hebrewword):
    cursor.execute('''
    INSERT INTO Words (englishword, hebrewword)
    VALUES (?, ?)
    ''', (englishword, hebrewword))
    conn.commit()



def capitalizeAndSort(words_list):
    return [(englishword[0].capitalize() + englishword[1:], hebrewword) for englishword, hebrewword in words_list]

def populateWords():
    file_name = ('example.csv')
    words_list = read_file_to_name_value_list(file_name, delimiter=",")
    word_listC = capitalizeAndSort(words_list)
    sorted_words = sorted(word_listC, key=lambda x: x[0])
    add_words_from_list(sorted_words)
    selectwords()

def add_words_from_list(words_list):
    for englishword, hebrewword in words_list:
        add_word(englishword, hebrewword)
       # print(englishword," ",hebrewword)

"""
createSqliteTables()
updateTable()
selectQuery()


#create the DB in case it doesn't exist
createSqliteTables()
#populateWords()
"""


