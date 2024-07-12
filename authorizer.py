from requests.auth import HTTPBasicAuth


class Authorizer:
    def __init__(self, user, password, auth_type):
        self.user = user
        self.password = password
        self._auth_type = auth_type
        self.headers = self._get_headers()

    def get_auth(self):
        return HTTPBasicAuth(self.user, self.password) if self._auth_type.__eq__('bearer') else None

    def _get_headers(self):
        headers = {
            "Accept": "application/json"
        }

        if self._auth_type.__eq__('bearer'):
            headers['Authorization'] = f'Bearer {self.password}'

        return headers
