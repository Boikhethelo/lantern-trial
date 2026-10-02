import sqlite3


class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connection(self):

        return sqlite3.connect(self.connection_string)

    def insert_question(self, room : str, difficulty : int, question : str, answer : str, hint: str, character: str):

        cursor = self.connection().cursor()
        cursor.execute("INSERT INTO questions (room,difficulty,question,answer,hint,character) VALUES (?,?,?,?,?,?,?) ",
                       (room, difficulty, question, answer, hint, character))
        self.connection().commit()
        print("inserted successfully" + cursor.lastrowid)
        self.connection().close()

    def read_schema(self):
        with open("/resources/schema.sql", "r" , encoding="utf-8") as file:
            schema = file.read()
            cursor = self.connection().cursor()

            try:
                cursor.executescript(schema)
                self.connection().commit()
                print("Database and schema successfully loaded")
            except sqlite3.Error as error:
                print(error)
            finally:
                self.connection().close()


    def get_question(self, room: str, difficulty) -> dict:


        cursor = self.connection().cursor()
        cursor.execute("SELECT * FROM questions WHERE room=? AND difficulty=? ORDER BY RANDOM() LIMIT 1",(room, difficulty))
        row = cursor.fetchone()
        output = {"question" : row[0], "answer" : row[1], "hint" : row[2], "character" : row[3]}
        self.connection().close()

        return output



