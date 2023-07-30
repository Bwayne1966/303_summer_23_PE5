# conftest.py
import time
import pytest

@pytest.fixture(autouse=True)
def timer():
    start = time.time()
    yield
    end = time.time()
    print("\nTest took: ", end - start, "seconds.")
