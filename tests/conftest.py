import pytest


@pytest.fixture
def example_string():
    return (
        "For example, the simple address /string/\n"
        "matches the next occurence of ''string'',\n"
        "not the next line containing ''string''.\n"
    )
