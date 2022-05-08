import abc


class Shape(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethode
    def calculate_area(self):
        pass

