from rescue_dog.lib.task import Task
from rescue_dog.lib.queue import Queue

class Groomer:
    def __init__(self):
        self.params = {
          'in_state': 'healthy',
          'out_state': 'groomed',
          'completion_time': 10,
        }
        self.dog = Queue().receive_from_queue(self.params['in_state'])

    def complete_task(self):
        t = Task(self.dog, self.params)
        self.dog = t.complete()
        return self.dog
