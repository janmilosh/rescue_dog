from mock import patch
from rescue_dog.roles.onboarder import Onboarder
from rescue_dog.roles.dog import Dog
from rescue_dog.lib.queue import Queue

ONBOARDED_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'onboarded',}

@patch.object(Dog, '_input_name', return_value = 'Sam')
@patch.object(Dog, '_input_age', return_value = '12')
@patch.object(Dog, '_input_breed', return_value = 'Beagle')
@patch.object(Queue, 'add_to_queue')
def test_onboarder_completes_task(*args, **kwargs):
    o = Onboarder()
    assert o.dog == ONBOARDED_DOG
    o.complete_task()
    Queue.add_to_queue.assert_called_with(o.dog)
