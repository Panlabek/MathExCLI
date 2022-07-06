from math_db import Math_db
from testing_helpers import create_dummy_db, create_dummy_exercise, create_rand_exercise, create_exercise_with_input
def test_exercise_class_test1():
    ex_number = 2
    ex1 = create_exercise_with_input(ex_number, 0, "")
    assert ex1.ex_number == ex_number
def test_exercise_class_test2():
    chapter = 3
    ex1 = create_exercise_with_input(0, chapter, "")
    assert ex1.chapter == chapter
def test_exercise_class_test3():
    status = "DONE"
    ex1 = create_exercise_with_input(0, 0, status)
    assert ex1.ex_status == status
def test_insert_exercise():
    ex = create_dummy_exercise()
    ex_db = Math_db(":memory:")
    ex_db.insert_exercise(ex)
    assert ex_db.fetch_all_exercises()[0] == ex.get_ex_as_tuple()
def test_remove_exercise():
    ex = create_rand_exercise()
    ex_db = create_dummy_db()
    ex_db.insert_exercise(ex)
    assert ex_db.fetch_all_exercises()[0] == ex.get_ex_as_tuple()
    ex_db.remove_exercise(ex)
    assert ex_db.fetch_all_exercises()[0] == ex.get_ex_as_tuple()
