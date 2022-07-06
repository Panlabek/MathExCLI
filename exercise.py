class Exercise():
    def __init__(self, ex_number=None, chapter=None, ex_status=None,date_finished=None):
        self.ex_number = ex_number
        self.chapter = chapter
        self.ex_status = ex_status
        self.date_finished = date_finished
    def __str__(self):
        return f"ex_number:{self.ex_number}, chapter:{self.chapter}, ex_status:{self.ex_status}, date_finished:{self.date_finished}"
