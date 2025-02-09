# populate table
# -------------------------#
from DBConnection import cursor, conn


def updateTableUsers():
    print("Start updateTableUsers:  ")
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    conn.commit()  # Save changes to the database


def updateTablewords():
    print("Start updateTablewords:  ")
    cursor.execute("INSERT INTO words (englishword, hebrewword) VALUES (?, ?)", ("go", "לך"))
    cursor.execute("INSERT INTO words (englishword, hebrewword) VALUES (?, ?)", ("come", "בוא"))
    cursor.execute("INSERT INTO words (englishword, hebrewword) VALUES (?, ?)", ("home", "בית"))
    conn.commit()  # Save changes to the database
