from copy import deepcopy

import httpx
import pytest

from src.app import app, activities


@pytest.fixture
def client():
    original_activities = deepcopy(activities)

    with httpx.Client(app=app, base_url="http://testserver") as client:
        yield client

    activities.clear()
    activities.update(original_activities)
