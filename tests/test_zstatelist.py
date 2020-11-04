from lipidhandler.zstatelist import ZstateList
from lipidhandler.zstate import Zstate


def test_zstatelist():
    zstatelist = ZstateList.parse("(9Z,6Z)")

    assert len(zstatelist) == 2
    for zstate in zstatelist:
        assert isinstance(zstate, Zstate)

    assert str(zstatelist[0]) == '9Z'
    assert str(zstatelist[1]) == '6Z'

    # try again with spaces
    zstatelist = ZstateList.parse("(9Z, 6Z)")

    assert len(zstatelist) == 2
    for zstate in zstatelist:
        assert isinstance(zstate, Zstate)

    assert str(zstatelist[0]) == '9Z'
    assert str(zstatelist[1]) == '6Z'
