from typing import Union


class Calculator:

    def __init__(self, number1, number2):
        self.number1: Union[int | float] = number1
        self.number2: Union[int | float] = number2

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Both elements must be numbers")
        if key == "number2" and value == 0:
            raise ZeroDivisionError("Number 2 can not be zero")
        self.__dict__[key] = value

    def add(self) -> int | float:
        return self.number1 + self.number2

    def subtract(self) -> int | float:
        return self.number1 - self.number2

    def multi(self) -> int | float:
        return self.number1 * self.number2

    def divide(self) -> int | float:
        return self.number1 / self.number2
