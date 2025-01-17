from datetime import datetime

import app.operations.operation_helpers as oh
import app.utils.helpers as h
from tests.client_fixtures import *
from tests.data_fixtures import *


def test_add_time():

    test_time = datetime(2000, 8, 23, 15, 30, 58, 800000)

    # Test Minutes
    res = h.add_time(test_time, "5n")
    assert res == datetime(2000, 8, 23, 15, 35, 58,
                           800000), f'Failed to add minutes'

    # Test Hours
    res = h.add_time(test_time, "5h")
    assert res == datetime(2000, 8, 23, 20, 30, 58,
                           800000), f'Failed to add hours'

    # Test Days
    res = h.add_time(test_time, "5d")
    assert res == datetime(2000, 8, 28, 15, 30, 58,
                           800000), f'Failed to add days'

    # Test Months
    res = h.add_time(test_time, "5m")
    assert res == datetime(2001, 1, 23, 15, 30, 58,
                           800000), f'Failed to add months'

    # Test Years
    res = h.add_time(test_time, "5y")
    assert res == datetime(2005, 8, 23, 15, 30, 58,
                           800000), f'Failed to add years'

    # Test zero case
    res = h.add_time(test_time, "0d")
    assert res == test_time, f'Altered time with zero increment'

    # Test broken case
    res = h.add_time(test_time, "99bb")
    assert res is None, f'Altered time with invalid frequency increment format'

    res = h.add_time(test_time, "5a")
    assert res is None, f'Altered time with invalid frequency increment format'
