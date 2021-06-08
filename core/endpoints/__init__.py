import random
import string


class UserData:

    def __init__(self, name=None, gender=None, email=None, status=None, **kwargs):
        self.name = name
        self.gender = gender
        self.email = email
        self.status = status
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def as_dict(self):
        return self.__dict__

    @staticmethod
    def generate_random_email(length=5):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for _ in range(length))
        return f'{result_str}@gl.testing.com'

    def __eq__(self, other):
        if isinstance(other, UserData):
            return self.as_dict == other.as_dict
        return False

    def __repr__(self):
        return "Foo({!r})".format(self.as_dict)
