from json import load
from asyncfinder import is_async_visit
import pytest

EXPECTED_RESULTS = [
    ("async_finder_tests/helloworld.py", False),
    ("async_finder_tests/await_in_asyncdef", False),
    ("async_finder_tests/naked_await.py", True),
    ("async_finder_tests/naked_asyncWith.py", True),
    ("async_finder_tests/naked_asyncFor.py", True),
    ("async_finder_tests/importasyncio.py", False),
    ("async_finder_tests/asyncio_comment.py", False),
]

def load_and_test(filename) -> bool:
    with open(filename, 'r') as infile:
        source = infile.read()

    return is_async_visit(source)

@pytest.mark.parametrize("file, result", EXPECTED_RESULTS)
def test_file_for_async(file, result):
    assert load_and_test(file) is result