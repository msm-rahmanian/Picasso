import abc


class Shape(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def calculate_area(self):
        pass

