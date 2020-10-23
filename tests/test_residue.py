from lipidhandler.residue import Residue


def test_residue_string():
    r = Residue(15, 3)
    assert r.residue_string == "15:3"

    r = Residue(15, 3, 2)
    assert r.residue_string == '15:3;2'

    r = Residue(15, 3, 2, True)
    assert r.residue_string == 'O-15:3;2'
