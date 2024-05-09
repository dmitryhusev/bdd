from pytest_bdd import given,when,then,scenarios
import requests


scenarios('./test2.feature')


@given('sign up to api2', target_fixture='signup')
def sign_up():
    res = requests.get('http://httpbin.org/get')
    url = res.json().get('url')
    token = res.json().get('headers').get('X-Amzn-Trace-Id')
    assert url == 'http://httpbin.org/get'
    return url, token


@when('login to api2', target_fixture='login')
def login(signup):
    url, token = signup
    res = requests.get(url, headers={'token': token})
    assert res.status_code == 200
    return {
        'is_authenticated': True
    }


@then('user is logged in2')
def logged_in(login):
    assert login.get('is_authenticated')
