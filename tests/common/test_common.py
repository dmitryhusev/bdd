import requests
import pytest
import os

def sign_up():
    res = requests.get('http://httpbin.org/get')
    url = res.json().get('url')
    token = res.json().get('headers').get('X-Amzn-Trace-Id')
    assert url == 'http://httpbin.org/get'
    return url, token


def login(url, token):
    res = requests.get(url, headers={'token': token})
    assert res.status_code == 200
    return {
        'is_authenticated': True
    }


@pytest.mark.web
def test_logged_in():
    url, token = sign_up()
    data = login(url, token)
    assert data.get('is_authenticated')
