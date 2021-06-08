from http import HTTPStatus

import pytest

from core.api_base import OAuth2Client
from core.endpoints import UserData
from core.endpoints.end_points import EndPoint


@pytest.fixture(scope='module')
def exp_user_to_update(response_as_json, get_user_by):
    user_data = response_as_json(get_user_by(genre='Active'))['data'][0]
    user = UserData(name='TestName', gender=user_data['gender'], email=user_data['email'], status='Inactive', id=user_data['id'])
    return user


@pytest.fixture(scope='module')
def update_user(exp_user_to_update):
    api = OAuth2Client()
    response = api.patch(EndPoint.UPDATE_USER_DETAILS_PATCH.value, exp_user_to_update.id, data=exp_user_to_update.as_dict)
    return response


def test_successful_response_code(update_user):
    assert update_user.status_code == HTTPStatus.OK, f'Expected status code is: {HTTPStatus.OK.value}'


def test_created_user_in_list_of_users(update_user, exp_user_to_update, get_user_by, response_as_json):
    # TODO: encapsulate it as fixture or method
    user_data = response_as_json(get_user_by(id=exp_user_to_update.id))['data'][0]
    actual_user = UserData(name=user_data['name'], gender=user_data['gender'],
                           email=user_data['email'], status=user_data['status'], id=user_data['id'])
    assert actual_user == exp_user_to_update, 'Correct user should be updated'
