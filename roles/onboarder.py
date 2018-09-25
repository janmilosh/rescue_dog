from rescue_dog.lib.queue import Queue
from rescue_dog.roles.dog import Dog

class Onboarder:
    def __init__(self):
        self.dog = Dog().intake()

    def complete_task(self):
        Queue().add_to_queue(self.dog)
        return self.dog
