import datetime
from math_db import Math_db
from random import randint
from testing_helpers import create_dummy_db, create_dummy_exercise, create_rand_exercise, create_exercise_with_input, rand_ex_status
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
    assert len(ex_db.fetch_all_exercises()) == 0
def test_get_exercises_by_num_and_chap():
    ex = create_rand_exercise()
    ex_db = create_dummy_db()
    ex_db.insert_exercise(ex)
    assert ex_db.get_exercises_by_num_and_chap(ex_number=ex.ex_number, chapter=ex.chapter)[0] == ex.get_ex_as_tuple()
def test_get_exercises_by_chap():
    ex = create_rand_exercise()
    ex_db = create_dummy_db()
    ex_db.insert_exercise(ex)
    assert ex_db.get_exercises_by_chap(chapter=ex.chapter)[0] == ex.get_ex_as_tuple()
def test_dummy_exercises_creation():
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    ex_db = create_dummy_db()
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    assert len(ex_db.fetch_all_exercises()) == (last_ex+1)
def test_update_ex_status_and_df():
    ex_db = create_dummy_db()
    ex = create_rand_exercise(datetime.datetime.now())
    df = ex_db.get_todays_date()
    status = rand_ex_status()
    ex_db.insert_exercise(ex)
    ex_db.update_ex_status_and_date_finished(new_status=status, new_date=df, ex_number=ex.ex_number, chapter=ex.chapter)
    ex.ex_status = status
    ex.date_finished = df
    assert ex_db.fetch_all_exercises()[0] == ex.get_ex_as_tuple()
def test_marking_status_as_done_for_every_ex():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    status = "DONE"
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    ex_db.mark_status_as_done_for_all_exercises(chapter)
    data = ex_db.fetch_all_exercises()
    for i in data:
        _,_,e_status,_ = i
        assert e_status == status
def test_fetching_exercises_from_given_range():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    data = ex_db.fetch_exercises_from_given_range(first_ex=first_ex, last_ex=last_ex, chapter=chapter)
    counter = 0
    for _ in data: counter += 1
    assert counter == (last_ex+1)
def test_marking_status_as_done_for_given_range():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    status = "DONE"
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    ex_db.mark_status_as_done_for_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    data = ex_db.fetch_exercises_from_given_range(first_ex=first_ex, last_ex=last_ex, chapter=chapter)
    for i in data:
        _,_,_e_status,_ = i
        assert _e_status == status
def test_fetch_finished_ex_from_given_chapter():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    ex_db.mark_status_as_done_for_all_exercises(chapter)
    assert len(ex_db.fetch_finished_ex_from_given_chapter(chapter=chapter)) == (last_ex+1)
def test_count_finished_ex_from_given_chapter():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    ex_db.mark_status_as_done_for_all_exercises(chapter)
    assert ex_db.count_finished_ex_from_given_chapter(chapter=chapter) == (last_ex+1)
def test_fetch_finished_ex_from_given_data():
    ex_db = create_dummy_db()
    ex_num = 12
    ex_chap = 32
    ex_status = "DONE"
    ex_df = ex_db.get_todays_date()
    ex = create_exercise_with_input(ex_number=ex_num,chapter=ex_chap, ex_status=ex_status, date_finished=ex_df)
    ex_db.insert_exercise(ex)
    assert len(ex_db.fetch_finished_ex_from_given_date(date=ex_db.get_todays_date())) == 1
    assert ex_db.fetch_finished_ex_from_given_date(date=ex_db.get_todays_date())[0] == ex.get_ex_as_tuple()
def test_fetch_all_exercises():
    ex_db = create_dummy_db()
    first_ex = 0
    last_ex = randint(7,100)
    chapter = randint(0,10)
    ex_db.create_dummy_exercises_for_chapter_given_range(first_exercise=first_ex, last_exercise=last_ex, chapter=chapter)
    assert len(ex_db.fetch_all_exercises()) == (last_ex+1)
def test_get_todays_date():
    tdate = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
    ex_db = create_dummy_db()
    assert ex_db.get_todays_date() == tdate
def test_count_ex_list():
    counter = 0
    ex_db = create_dummy_db()
    lister = [x for x in range (20)]
    for _ in lister:
        counter += 1
    assert ex_db.count_exercise_list(lister) == counter
