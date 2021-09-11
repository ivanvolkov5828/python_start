class Worker:
    name = "Иван"
    surname = "Волков"
    position = "Student"
    _income = {"wage": 120000, "bonus": 45000}


class Position(Worker):

    def __init__(self, name, surname, position, my_dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = my_dict

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Заработная плата: {self._income["wage"]}')
        print(f'Премия: {self._income["bonus"]}')


income = {"wage": 30000, "bonus": 5000}

position_1 = Position("Дарья", "Вовчук", "Бариста", income)
position_1.get_full_name()
position_1.get_total_income()
