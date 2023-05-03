import requests
from urllib.parse import urlencode


class AnySolve(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.anysolve.ai/rest/v1/tasks/{}/{}"

    def run(self, task_slug, version, parameters):
        url = self.base_url.format(task_slug, version)

        if len(parameters) > 0:
            url = f"{url}?{urlencode(parameters)}"

        headers = {"Content-Type": "application/json"}

        res = requests.get(url, headers=headers, auth=BearerAuth(self.api_key)).json()

        if "error" in res:
            raise Exception(res["error"])

        return res


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.api_key
        return r
