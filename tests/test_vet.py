from mock import patch, MagicMock
from rescue_dog.roles.vet import Vet
from rescue_dog.lib.queue import Queue
from rescue_dog.lib.task import Task

ONBOARDED_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'onboarded',}
HEALTHY_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'healthy',}
PARAMS = {'in_state': 'onboarded', 'out_state': 'healthy', 'completion_time': 5,}

@patch.object(Queue, 'receive_from_queue')
@patch.object(Queue, 'add_to_queue')
@patch.object(Task, '_do_work')
def test_vet_completes_task(*args, **kwargs):
    Queue.receive_from_queue = MagicMock(return_value = ONBOARDED_DOG)
    v = Vet()
    v.complete_task()
    assert v.dog == HEALTHY_DOG
    Queue.receive_from_queue.assert_called_with('onboarded')
    Queue.add_to_queue.assert_called_with(v.dog)
