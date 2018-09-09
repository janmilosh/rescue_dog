class Onboarder:
    def __init__(self):
        self.dog = {'name': None, 'age': None, 'breed': None, 'state': 'onboarded'}

    def complete_task(self):
        self.intake()
        self.add_to_queue()
        return self.dog

    def intake(self):
        self.dog['name'] = self.input_name()
        self.dog['age'] = self.input_age()
        self.dog['breed'] = self.input_breed()
        return True

    def input_name(self):
        return input("Dog's name: ")

    def input_age(self):
        return input("Dog's age: ")

    def input_breed(self):
        return input("Dog's breed: ")

    def add_to_queue(self):
        pass

if __name__ == "__main__":
    o = Onboarder()
    o.complete_task()
