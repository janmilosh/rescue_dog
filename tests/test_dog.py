from mock import patch
from rescue_dog.roles.dog import Dog
from rescue_dog.lib.queue import Queue

INITIAL_DOG = {'name': None, 'age': None, 'breed': None, 'state': 'onboarded',}
ONBOARDED_DOG = {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'onboarded',}

@patch.object(Dog, '_input_name', return_value = 'Sam')
@patch.object(Dog, '_input_age', return_value = '12')
@patch.object(Dog, '_input_breed', return_value = 'Beagle')
def test_intake_dog(*args, **kwargs):
    d = Dog()
    assert d.dog == INITIAL_DOG
    d.intake()
    assert d.dog == ONBOARDED_DOG
