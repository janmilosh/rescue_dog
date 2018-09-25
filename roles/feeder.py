from rescue_dog.lib.task import Task
from rescue_dog.lib.queue import Queue

class Feeder:
    def __init__(self):
        self.params = {
          'in_state': 'groomed',
          'out_state': 'ate',
          'completion_time': 3,
        }
        self.dog = Queue().receive_from_queue(self.params['in_state'])

    def complete_task(self):
        t = Task(self.dog, self.params)
        self.dog = t.complete()
        return self.dog
