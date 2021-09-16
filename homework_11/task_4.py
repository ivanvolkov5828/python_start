# класс описывающий склад
class Warehouse:
    pass


# класс Оргтехника
class OfficeEquipment:
    def __init__(self, price, year_of_release):
        self.price = price
        self.year_of_release = year_of_release


# класс принтер
class Printer(OfficeEquipment):
    def __init__(self, price, year_of_release, print_speed):
        super().__init__(price, year_of_release)
        self.print_speed = print_speed


# класс сканер
class Scanner(OfficeEquipment):
    def __init__(self, price, year_of_release, scanner_speed):
        super().__init__(price, year_of_release)
        self.scanner_speed = scanner_speed


# класс ксерокс
class Xerox(OfficeEquipment):
    def __init__(self, price, year_of_release, xerox_speed):
        super().__init__(price, year_of_release)
        self.xerox_speed = xerox_speed
