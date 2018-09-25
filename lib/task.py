from rescue_dog.lib.queue import Queue
import time

class Task:
    def __init__(self, dog, params):
        self.dog = dog
        self.params = params

    def complete(self):
        self._do_work()
        self._update_state()
        Queue.add_to_queue(self.dog)
        return self.dog

    def _do_work(self):
        time.sleep(self.params['completion_time'])
        return f"Task took {self.params['completion_time']} seconds"

    def _update_state(self):
        self.dog['state'] = self.params['out_state']
        return True
