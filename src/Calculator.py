def addition(a,b):
    return a+b


class Calculator:

    result = 0

    def add(self, a, b):
        self.result = a + b
        return addition(a,b)


    def __init__(self):
        x = 2 + 2
        self.result = x
        pass