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


    def get_question(self, room: str, difficulty: int, character: str) -> dict :
        conn = self.connection()
        conn.row_factory = sqlite3.Row
        try:
            row = conn.execute(
                """
                SELECT id, room, difficulty, question, answer,
                       CASE WHEN character IS NULL OR character = ? THEN hint END AS hint
                FROM questions
                WHERE room = ?
                ORDER BY ABS(difficulty - ?), RANDOM()
                LIMIT 1
                """,
                (character, room, difficulty),
            ).fetchone()
        finally:
            conn.close()

        return dict(row)



