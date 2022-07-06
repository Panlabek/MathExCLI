from exercise import Exercise
from math_db import Math_db
from random import randint
def create_dummy_db():
    return Math_db(":memory:")
def create_dummy_exercise():
    return Exercise()
def create_rand_exercise():
    todo_opts = ["DONE", "FAILED", "TODO", "PLANNED"]
    return Exercise(ex_number=randint(0,100), chapter=randint(0,100), ex_status=todo_opts[randint(0,3)])
def create_exercise_with_input(ex_number:int, chapter:int, ex_status:str, date_finished=None):
    return Exercise(ex_number=ex_number, chapter=chapter, ex_status=ex_status, date_finished=date_finished)
