import pytest
import os

def pytest_bdd_apply_tag(tag, function):
    if tag == 'ui':
        marker = pytest.mark.skip(reason='Skipped for now')
        marker(function)
        return True
    else:
        return None