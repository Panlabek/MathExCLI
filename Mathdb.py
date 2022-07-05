import sqlite3
from exercise import Exercise
import datetime
class MathDb():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"{db_name}")
        self.c = self.conn.cursor()
        # self.c.execute("""CREATE TABLE exercises (
        #             chapter integer,
        #             ex_number integer,
        #             ex_status text,
        #             date_finished text
        #             )""")
    def insert_exercise(self, exercise):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter": exercise.chapter, "ex_number": exercise.ex_number})
        ex_list = self.c.fetchall()
        if len(ex_list) == 0:
            with self.conn:
                self.c.execute("INSERT INTO exercises VALUES (:chapter, :ex_number, :ex_status, :date_finished)", {"chapter": exercise.chapter, "ex_number": exercise.ex_number, "ex_status": exercise.ex_status, "date_finished": exercise.date_finished})
        else:
            self.update_ex_status_and_date_finished(new_status=exercise.ex_status, new_date=exercise.date_finished, ex_number=exercise.ex_number, chapter=exercise.chapter)
    def remove_exercise(self,exercise):
        with self.conn:
            self.c.execute("DELETE from exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter":exercise.chapter, "ex_number": exercise.ex_number})
    def get_exercises_by_num_and_chap(self, ex_number: int, chapter: int):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter": chapter, "ex_number": ex_number})
        return self.c.fetchall()
    def get_exercises_by_chap(self,chapter: int):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter", {"chapter": chapter})
        return self.c.fetchall()
    def create_dummy_exercises_for_chapter_given_range(self, first_exercise: int, last_exercise: int, chapter: int):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter": chapter})
        list_ex = self.c.fetchall()
        if len(list_ex) == 0:
            with self.conn:
                for i in range(first_exercise, last_exercise+1):
                    dummy_exercise = Exercise(i, chapter, "TODO", None)
                    self.c.execute("INSERT INTO exercises VALUES (:chapter, :ex_number, :ex_status, :date_finished)", {"chapter": dummy_exercise.chapter, "ex_number": dummy_exercise.ex_number, "ex_status": dummy_exercise.ex_status, "date_finished": dummy_exercise.date_finished})
        else:
            pass
    def update_ex_status_and_date_finished(self,new_status: str, new_date, ex_number: int, chapter: int):
        with self.conn:
            self.c.execute("""UPDATE exercises SET ex_status = :ex_status WHERE ex_number = :ex_number AND chapter = :chapter""",
                        {"ex_status": new_status,"ex_number": ex_number, "chapter": chapter})
            self.c.execute("""UPDATE exercises SET date_finished = :date_finished WHERE ex_number = :ex_number AND chapter = :chapter""",
                        {"ex_number": ex_number, "date_finished": new_date, "chapter": chapter})

    def mark_status_as_done_for_all_exercises(self,chapter: int):
        with self.conn:
            self.c.execute("""UPDATE exercises SET ex_status = :ex_status WHERE chapter = :chapter""", {"ex_status": "DONE", "chapter": chapter})
            self.c.execute("""UPDATE exercises SET date_finished = :date_finished WHERE chapter = :chapter""",
                        {"date_finished": self.get_todays_date(), "chapter": chapter})

    def mark_status_as_done_for_given_range(self,first_exercise: int, last_exercise, chapter):
        with self.conn:
            for i in range(first_exercise, last_exercise+1):
                self.c.execute("""UPDATE exercises SET ex_status = :ex_status WHERE ex_number = :ex_number AND chapter = :chapter""",
                            {"ex_status": "DONE","ex_number": i, "chapter": chapter})
                self.c.execute("""UPDATE exercises SET date_finished = :date_finished WHERE ex_number = :ex_number AND chapter = :chapter""",
                            {"ex_number": i, "date_finished": self.get_todays_date(), "chapter": chapter})

    def fetch_finished_ex_from_given_chapter(self,chapter: int):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_status = 'DONE'", {"chapter": chapter})
        return self.c.fetchall()
    def count_finished_ex_from_given_chapter(self, chapter: int):
        self.c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_status = 'DONE'", {"chapter": chapter})
        ex_list = self.c.fetchall()
        return self.count_exercise_list(ex_list)

    def get_todays_date(self):
        return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")

    def count_exercise_list(self,c: list):
        count = 0
        for _ in c:
            count +=1
        return count

    def fetch_finished_ex_from_given_date(self,date):
        self.c.execute("""SELECT * FROM exercises WHERE date_finished = :date""",
                {"date": date})
        return self.c.fetchall()
    def __del__(self):
        self.conn.close()
