import pytest
from mock import patch

from rescue_dog.roles.onboarder import Onboarder

@patch.object(Onboarder, 'input_name', return_value = 'Sam')
@patch.object(Onboarder, 'input_age', return_value = '12')
@patch.object(Onboarder, 'input_breed', return_value = 'Beagle')
def test_onboarding_dog(*args, **kwargs):
    dog = Onboarder().complete_task()
    assert dog == {'name': 'Sam', 'age': '12', 'breed': 'Beagle', 'state': 'onboarded'}
