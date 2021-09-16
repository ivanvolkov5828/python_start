class Warehouse:
    def __init__(self, *technic):
        self.technic = list(technic)

    def my_list(self):
        return self.technic

    def quantity(self):
        return dict((el, self.technic.count(el)) for el in set(self.technic))


class OfficeEquipment:
    def __init__(self, price, year_of_release):
        self.price = price
        self.year_of_release = year_of_release


class Printer(OfficeEquipment):
    def __init__(self, price, year_of_release, print_speed):
        super().__init__(price, year_of_release)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, price, year_of_release, scanner_speed):
        super().__init__(price, year_of_release)
        self.scanner_speed = scanner_speed


class Xerox(OfficeEquipment):
    def __init__(self, price, year_of_release, xerox_speed):
        super().__init__(price, year_of_release)
        self.xerox_speed = xerox_speed


warehouse = Warehouse("Printer", "Scanner", "Xerox", "Printer", "Scanner", "Xerox", "Scanner", "Xerox")

print(warehouse.my_list())
print(warehouse.quantity())
