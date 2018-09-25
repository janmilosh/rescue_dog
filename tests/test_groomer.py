from mock import patch, MagicMock
from rescue_dog.roles.groomer import Groomer
from rescue_dog.lib.queue import Queue
from rescue_dog.lib.task import Task

HEALTHY_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'healthy',}
GROOMED_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'groomed',}
PARAMS = {'in_state': 'healthy', 'out_state': 'groomed', 'completion_time': 10,}

@patch.object(Queue, 'receive_from_queue')
@patch.object(Queue, 'add_to_queue')
@patch.object(Task, '_do_work')
def test_groomer_completes_task(*args, **kwargs):
    Queue.receive_from_queue = MagicMock(return_value = HEALTHY_DOG)
    g = Groomer()
    g.complete_task()
    assert g.dog == GROOMED_DOG
    Queue.receive_from_queue.assert_called_with('healthy')
    Queue.add_to_queue.assert_called_with(g.dog)
