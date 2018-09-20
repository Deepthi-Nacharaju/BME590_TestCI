# Testing First Python
def test_add_three():
    from first_python import add_three
    s = add_three(1, 2, 3)
    assert s == 6


def test_div_three():
    from first_python import div_three
    p = div_three(6)
    assert p == 2
