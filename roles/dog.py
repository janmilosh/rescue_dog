class Dog:
    def __init__(self):
        self.dog = {'name': None, 'age': None, 'breed': None, 'state': 'onboarded'}

    def intake(self):
        self.dog['name'] = self._input_name()
        self.dog['age'] = self._input_age()
        self.dog['breed'] = self._input_breed()
        return self.dog

    def _input_name(self):
        return input("Dog's name: ")

    def _input_age(self):
        return input("Dog's age: ")

    def _input_breed(self):
        return input("Dog's breed: ")
