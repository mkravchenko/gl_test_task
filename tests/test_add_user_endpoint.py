from http import HTTPStatus

import pytest
from core.api_base import OAuth2Client
from jsonschema import validate

from core.endpoints import UserData
from core.endpoints.end_points import EndPoint
from core.schemas import Schema


@pytest.fixture(scope='module')
def exp_user():
    email = UserData.generate_random_email()
    user = UserData(name="GLTest", gender="Male", email=email, status="Active")
    return user


@pytest.fixture(scope='module')
def crete_new_user(exp_user):
    api = OAuth2Client()
    response = api.post(end_point=EndPoint.CREATE_NEW_USER_POST.value,
                        data=exp_user.as_dict)
    return response


def test_successful_response_code(crete_new_user):
    assert crete_new_user.status_code == HTTPStatus.OK, f'Expected status code is: {HTTPStatus.OK.value}'


def test_successful_response_validate_schema(crete_new_user, response_as_json):
    validate(response_as_json(crete_new_user), schema=Schema.CRETATE_NEW_USER_SCHEMA.value)


def test_created_user_in_list_of_users(crete_new_user, exp_user, get_user_by, response_as_json):
    # TODO: encapsulate it as fixture or method
    user_data = response_as_json(get_user_by(email=exp_user.email))['data'][0]
    actual_user = UserData(name=user_data['name'], gender=user_data['gender'], email=user_data['email'], status=user_data['status'])
    assert actual_user == exp_user, 'Correct user should be created'
