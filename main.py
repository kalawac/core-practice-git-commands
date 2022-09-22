import pytest


def always_returns_true():
<<<<<<< HEAD
    x = 2
    if x < 5:
        return True
    else:
        return False
=======
    return None
>>>>>>> 74141686ac15fcae9d3912fe26b7479b29ef6688


def test_always_returns_true():
    assert always_returns_true()
