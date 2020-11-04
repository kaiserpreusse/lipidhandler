from lipidhandler.zstate import Zstate


def test_zstate():
    zstate = Zstate.parse('9Z')

    assert str(zstate) == '9Z'
