from http import HTTPStatus

import pytest

from core.api_base import OAuth2Client
from core.endpoints import UserData
from core.endpoints.end_points import EndPoint


@pytest.fixture(scope='module')
def exp_user_to_delete(response_as_json, get_user_by):
    user_data = response_as_json(get_user_by(genre='Male'))['data'][0]
    user = UserData(name=user_data['name'], gender=user_data['gender'], email=user_data['email'], status=user_data['status'], id=user_data['id'])
    return user


@pytest.fixture(scope='module')
def remove_user(exp_user_to_delete):
    api = OAuth2Client()
    response = api.delete(EndPoint.DELETE_USER.value, exp_user_to_delete.id)
    return response


def test_successful_response_code(remove_user):
    assert remove_user.status_code == HTTPStatus.OK, f'Expected status code is: {HTTPStatus.OK.value}'


def test_check_no_deleted_user(remove_user, exp_user_to_delete, get_user_by, response_as_json, ensure):
    assert response_as_json(get_user_by(exp_user_to_delete.id))['code'] == HTTPStatus.NOT_FOUND, \
        f'Expected status code is: {HTTPStatus.NOT_FOUND.value}'
