from pytest_bdd import given,when,then,scenario
import requests
import pytest


@pytest.mark.skipif(1>0, reason="Reason")
@scenario('test.feature', 'user sign up and login')
def test_user():
    pass


@given('sign up to api', target_fixture='signup')
def sign_up():
    res = requests.get('http://httpbin.org/get')
    url = res.json().get('url')
    token = res.json().get('headers').get('X-Amzn-Trace-Id')
    assert url == 'http://httpbin.org/get'
    return url, token


@when('login to api', target_fixture='login')
def login(signup):
    url, token = signup
    res = requests.get(url, headers={'token': token})
    assert res.status_code == 200
    return {
        'is_authenticated': True
    }


@then('user is logged in')
def logged_in(login):
    assert login.get('is_authenticated')
