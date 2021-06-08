import json

import pytest
from helper import wait_until

from core.api_base import CoreApiClient
from core.endpoints.end_points import EndPoint


@pytest.fixture(scope='module')
def response_as_json():
    def func(response):
        return json.loads(response.text)

    return func


@pytest.fixture(scope='module')
def ppjson():
    def func(text, indent=10, sort_keys=True):
        print(json.dumps(text, indent=indent, sort_keys=sort_keys))

    return func


@pytest.fixture(scope='module')
def get_user_by():
    def func(*args, **kwargs):
        base_api = CoreApiClient()
        response = base_api.get(EndPoint.GET_USER_DETAILS_GET.value, *args, **kwargs)
        return response

    return func


@pytest.fixture(scope='module')
def ensure():
    return wait_until
