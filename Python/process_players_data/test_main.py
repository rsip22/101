from .main import q_1, q_2, q_3, q_4, q_5, q_6

# Challenge validation tests


def test_1():
    assert isinstance(q_1(), int)


def test_2():
    assert isinstance(q_2(), int)


def test_3():
    r = q_3()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )


def test_4():
    r = q_4()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )


def test_5():
    r = q_5()
    assert (
        isinstance(r, list) and
        all(isinstance(y, str) for y in r)
    )


def test_6():
    r = q_6()
    assert (
        isinstance(r, dict) and
        all(isinstance(y, int) for y in r.keys()) and
        all(isinstance(y, int) for y in r.values())
    )
