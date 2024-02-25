import time
import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session"""
    yield
    now = time.time()
    print('--')
    print('finished: {}'.format('%d %b %x', time.localtime(now)))
    print('-------------')
