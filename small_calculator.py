class SmallCalculator:
    def __init__(self, initial_value):
        self.value = initial_value

    def increment_by_one(self):
        self.value += 1
        return self.value

    def increment_by_amount(self, amount):
        self.value += amount
        return self.value

    def decrement_by_one(self):
        self.value -= 1
        return self.value

    def decrement_by_amount(self, amount):
        self.value -= amount
        return self.value

    def current_value(self):
        return self.value
