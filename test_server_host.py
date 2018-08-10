"""test_server_host.py

"""
import pytest


@pytest.fixture(scope="module")
def fixture():
    return "hello world"


class TestServerHost:

    def test_something(self, fixture):
        print(f"Fixture: {fixture}")

        assert 1 == 1
