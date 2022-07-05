from Mathdb import MathDb
from pprint import pprint

from exercise import Exercise
def main():
    Db = MathDb("mather.db")
    exercisers = Db.count_finished_ex_from_given_chapter(4)
    pprint(exercisers)
if __name__ == "__main__":
    main()
