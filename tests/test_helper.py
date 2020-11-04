from lipidhandler.helper import rreplace, remove_outside_brackets


def test_rreplace():
    out = rreplace('(ABC(D)EFG)', ')', '', 1)

    assert out == '(ABC(D)EFG'

    out = rreplace('ABCxDEFxHIJxKLM', 'x', 'y', 2)

    assert out == 'ABCxDEFyHIJyKLM'


def test_remove_outside_brackets():

    out = remove_outside_brackets("(ABCD)")
    assert out == "ABCD"

    out = remove_outside_brackets("A(B)C")
    assert out == 'A(B)C'
