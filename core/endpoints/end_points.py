from enum import Enum


class EndPoint(Enum):
    CREATE_NEW_USER_POST = '/users'
    GET_USER_DETAILS_GET = '/users'
    UPDATE_USER_DETAILS_PATCH = '/users'
    UPDATE_USER_DETAILS_PUT = '/users'
    DELETE_USER = '/users'
    OPTIONS = '/users'
    HEADER_ONLY = '/users'
