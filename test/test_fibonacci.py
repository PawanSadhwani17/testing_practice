import sys
sys.path.append("../")
from src.fabonacci import Fibonacci
import pytest

@pytest.mark.parametrize("value,expected", [(-1, "Incorrect input"), (0, 0),
                                            (1, 1),(3, 2)])
def test_fibonacci(value,expected):
    assert Fibonacci(value) == expected