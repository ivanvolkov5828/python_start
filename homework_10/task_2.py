from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    @abstractmethod
    def coat_fabric(self):
        # метод для подсчета расхода ткани на пальто
        pass

    @abstractmethod
    def fabric_suit(self):
        # метод для подсчета расхода ткани на костюм
        pass


class CoatAbstract(ClothesAbstract):
    # класс пальто в котором будет считаться расход для пальто
    @abstractmethod
    def __init__(self, V):
        pass

    @abstractmethod
    def coat_fabric(self):
        pass


class SuitAbstract(ClothesAbstract):
    # класс костюм в которм будет считаться расход для костюма
    @abstractmethod
    def __init__(self, H):
        pass

    @abstractmethod
    def fabric_suit(self):
        # метод для подсчета расхода ткани на костюм
        pass


# ----------------------------------------------->
# ----------------------------------------------->


class Clothes(ClothesAbstract):
    def coat_fabric(self):
        print("метод для подсчета расхода ткани на пальто")

    def fabric_suit(self):
        print("метод для подсчета расхода ткани на костюм")


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def coat_fabric(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def fabric_suit(self):
        return 2 * self.h + 0.3


coat = Coat(19.5)
suit = Suit(8)

print(coat.coat_fabric)
print(suit.fabric_suit)

print(f"Общий подсчёт расхода ткани: {coat.coat_fabric + suit.fabric_suit}")
