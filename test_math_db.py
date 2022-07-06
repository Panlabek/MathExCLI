from math_db import Math_db
from exercise import Exercise

def test_exercise_class_test1():
    ex_number = 2
    ex1 = Exercise(ex_number=ex_number)
    assert ex1.ex_number == ex_number
def test_exercise_class_test2():
    chapter = 3
    ex1 = Exercise(chapter=chapter)
    assert ex1.chapter == chapter
def test_exercise_class_test3():
    status = "DONE"
    ex1 = Exercise(ex_status=status)
    assert ex1.ex_status == status
def test_insert_test():
    ex = Exercise()
    ex_db = Math_db(":memory:")
    ex_db.insert_exercise(ex)
    ret = ex_db.fetch_all_exercises()
    assert ret[0][0] == ex.ex_number
    assert ret[0][1] == ex.chapter
    assert ret[0][2] == ex.ex_status
    assert ret[0][3] == ex.date_finished
