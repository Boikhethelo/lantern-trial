import sqlite3


class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string


    def connection(self):

        return sqlite3.connect(self.connection_string)

    def insert_question(self, room : str, difficulty : int, question : str, answer : str, hint: str, character: str):


        conn = self.connection()

        cursor = conn.cursor()
        cursor.execute("INSERT INTO questions (room,difficulty,question,answer,hint,character) VALUES (?,?,?,?,?,?) ",
                       (room, difficulty, question, answer, hint, character))
        conn.commit()
        conn.close()

    def read_schema(self):
        with open("resources/schema.sql", "r" , encoding="utf-8") as file:
            schema = file.read()
            conn = self.connection()
            cursor = conn.cursor()

            try:
                cursor.executescript(schema)
                conn.commit()
                print("Database and schema successfully loaded")
            except sqlite3.Error as error:
                print(error)
            finally:
                conn.close()


    def get_question(self, room: str, difficulty:int) -> dict:

        conn = self.connection()


        cursor = conn.cursor()
        cursor.execute("SELECT * FROM questions WHERE room=? AND difficulty=? ORDER BY RANDOM() LIMIT 1",(room, str(difficulty)))
        row = cursor.fetchone()
        output = {"id"  : int(row[0]) , "room" : row[1], "difficulty" : int(row[2]), "question" : row[3] , "answer" : row[4] , "hint" : row[5] , "character" : row[6]}
        conn.close()

        return output



