from mock import patch, MagicMock
from rescue_dog.roles.feeder import Feeder
from rescue_dog.lib.queue import Queue
from rescue_dog.lib.task import Task

GROOMED_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'groomed',}
ATE_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'ate',}
PARAMS = {'in_state': 'groomed', 'out_state': 'ate', 'completion_time': 3,}

@patch.object(Queue, 'receive_from_queue')
@patch.object(Queue, 'add_to_queue')
@patch.object(Task, '_do_work')
def test_feeder_completes_task(*args, **kwargs):
    Queue.receive_from_queue = MagicMock(return_value = GROOMED_DOG)
    f = Feeder()
    f.complete_task()
    assert f.dog == ATE_DOG
    Queue.receive_from_queue.assert_called_with('groomed')
    Queue.add_to_queue.assert_called_with(f.dog)
