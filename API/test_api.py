import pytest
import requests
import json

@pytest.fixture()
def main_url():
    return "https://reqres.in"


def test_api(main_url):
    url = main_url + "/api/login/"
    # data = {'email': 'abc@xyz.com', 'password': 'qwerty'}
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == 'QpwL5tke4Pnpja7X4'
