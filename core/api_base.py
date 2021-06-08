import requests
from requests.sessions import Session

import config


class CoreApiClient:
    DEFAULT_HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, headers=None, **kwargs):
        self.headers = headers or self.DEFAULT_HEADERS
        self._session = None

    @property
    def session(self) -> Session:
        if not self._session:
            session = requests.Session()
            session.headers = self.headers
            self._session = session
        return self._session

    def create_url_params(self, *args, **kwargs):
        if args:
            param = '/'.join([f'{value}' for value in args])
            return f'/{param}'
        param = '&'.join([f'{key}={value}' for key, value in kwargs.items()])
        return f'?{param}' if param else param

    def create_url(self, end_point, *args, **kwargs):
        params = self.create_url_params(*args, **kwargs)
        url = '{}{}{}'.format(config.options['api']['url'], end_point, params)
        print(url)
        return url

    def get(self, end_point, *args, **kwargs):
        url = self.create_url(end_point, *args, **kwargs)
        return self.session.get(url)

    def post(self, end_point, data=None, **kwargs):
        url = self.create_url(end_point)
        return self.session.post(url, json=data)

    def delete(self, end_point, *args, **kwargs):
        url = self.create_url(end_point, *args, **kwargs)
        return self.session.delete(url)

    def update(self, end_point, data=None, **kwargs):
        url = self.create_url(end_point)
        return self.session.update(url, json=data)

    def patch(self, end_point, *args, data=None, **kwargs):
        url = self.create_url(end_point, *args, **kwargs)
        return self.session.patch(url, json=data)

    def headers(self, end_point, data=None, **kwargs):
        url = self.create_url(end_point)
        return self.session.headers(url, json=data)


class OAuth2Client(CoreApiClient):

    def __init__(self, token=None, headers=None, **kwargs):
        super().__init__(headers=headers, **kwargs)
        self.token = token or config.options['auth']['token']

    @property
    def session(self) -> Session:
        if not self._session:
            session = requests.Session()
            self.headers.update({'Authorization': f'Bearer {self.token}'})
            session.headers = self.headers
            self._session = session
        return self._session
