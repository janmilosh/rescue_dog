from mock import patch, MagicMock
from rescue_dog.roles.notifier import Notifier
from rescue_dog.lib.queue import Queue
from rescue_dog.lib.task import Task

ATE_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'ate',}
READY_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'Ready for a home',}
PARAMS = {'in_state': 'ate', 'out_state': 'Ready for home', 'completion_time': 2,}

@patch.object(Queue, 'add_to_queue')
@patch.object(Queue, 'receive_from_queue')
@patch.object(Task, '_do_work')
def test_notifier_completes_task(*args, **kwargs):
    Queue.receive_from_queue = MagicMock(return_value = ATE_DOG)
    n = Notifier()
    n.complete_task()
    assert n.dog == READY_DOG
    Queue.receive_from_queue.assert_called_with('ate')
    Queue.add_to_queue.assert_called_with(n.dog)
