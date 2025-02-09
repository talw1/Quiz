from DBConnection import cursor,conn,sqlite3

# set up data base table
# -------------------------#
def createSqliteTables():
    try:
        print("Start CREATE TABLE users  ")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')

        print("Start CREATE TABLE words  ")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            englishword TEXT NOT NULL,
            hebrewword TEXT NOT NULL,
            englishtransaltion TEXT,
            examtype TEXT NOT NULL
            )
        ''')

        print("Start CREATE TABLE quizresults  ")
        cursor.execute('''
            CREATE TABLE quizresults (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word_id INTEGER,
                user_answer TEXT,
                is_correct BOOLEAN,
                FOREIGN KEY (word_id) REFERENCES Words(id)
            )
        ''')
        print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        if "already exists" in str(e):
            print("Table already exists.")
        else:
            print(f"An error occurred: {e}")
