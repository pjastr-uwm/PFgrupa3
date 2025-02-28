class Calculator:

    def add(self, x, y):
        return x + y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y
