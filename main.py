import pytest


def always_returns_true():
    x = 2
    if x < 5:
        return True
    else:
        return False

def test_always_returns_true():
    assert always_returns_true()
