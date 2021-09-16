import re
import datetime


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transformation(cls):
        pattern = re.compile(r"\d{2,}")
        result = pattern.findall(cls("16.09.2021").date)
        result_int_gen = [int(el) for el in result]
        print(result_int_gen)

    @staticmethod
    def check(self):
        try:
            return datetime.datetime.strptime(self.date, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")


first = Date("16.09.2021")
first.transformation()
print(first.check(first))
