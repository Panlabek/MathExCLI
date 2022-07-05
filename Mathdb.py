import sqlite3
from exercise import Exercise
import datetime
from pprint import pprint

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("""CREATE TABLE exercises (
            chapter integer,
            ex_number integer,
            ex_status text,
            date_finished text
            )""")
def insert_exercise(exercise):
    with conn:
        c.execute("INSERT INTO exercises VALUES (:chapter, :ex_number, :ex_status, :date_finished)", {"chapter": exercise.chapter, "ex_number": exercise.ex_number, "ex_status": exercise.ex_status, "date_finished": exercise.date_finished})
def remove_exercise(exercise):
    with conn:
        c.execute("DELETE from exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter":exercise.chapter, "ex_number": exercise.ex_number})
def get_exercises_by_num_and_chap(ex_number: int, chapter: int):
    c.execute("SELECT * FROM exercises WHERE chapter = :chapter AND ex_number = :ex_number", {"chapter": chapter, "ex_number": ex_number})
    return c.fetchall()
def get_exercises_by_chap(chapter: int):
    c.execute("SELECT * FROM exercises WHERE chapter = :chapter", {"chapter": chapter})
    return c.fetchall()
def create_dummy_exercises_for_chapter_given_range(first_exercise: int, last_exercise: int, chapter: int):
    with conn:
        for i in range(first_exercise, last_exercise+1):
            dummy_exercise = Exercise(i, chapter, "TODO", None)
            c.execute("INSERT INTO exercises VALUES (:chapter, :ex_number, :ex_status, :date_finished)", {"chapter": dummy_exercise.chapter, "ex_number": dummy_exercise.ex_number, "ex_status": dummy_exercise.ex_status, "date_finished": dummy_exercise.date_finished})
def update_ex_status_and_date_finished(new_status: str, new_date, ex_number: int, chapter: int):
    with conn:
        c.execute("""UPDATE exercises SET ex_status = :ex_status WHERE ex_number = :ex_number AND chapter = :chapter""",
                    {"ex_status": new_status,"ex_number": ex_number, "chapter": chapter})
        c.execute("""UPDATE exercises SET date_finished = :date_finished WHERE ex_number = :ex_number AND chapter = :chapter""",
                    {"ex_status": new_status,"ex_number": ex_number, "date_finished": new_date, "chapter": chapter})
def mark_all_exercises_from_chapter_as_done(chapter: int):
    with conn:
        c.execute("""UPDATE exercises SET ex_status = :ex_status WHERE chapter = :chapter""", {"ex_status": "DONE", "chapter": chapter})

# exer1 = Exercise(32, 5, "DONE", datetime.datetime.now())
# insert_exercise(exer1)
create_dummy_exercises_for_chapter_given_range(0, 150, 5)
exercisers = get_exercises_by_chap(5)
pprint(exercisers)
# update_ex_status_and_date_finished(new_status="DONE", new_date=datetime.datetime.now(), ex_number=15, chapter=5)
# exercisers = get_exercises_by_num_and_chap(15,5)
# pprint(exercisers)
exercisers = get_exercises_by_chap(5)
pprint(exercisers)
conn.close()
