from lipidhandler.residue import Residue
from lipidhandler.residuemodification import ResidueModification


def test_residue_string():
    r = Residue(15, 3)
    assert r.residue_string == "15:3"

    r = Residue(15, 3, 2)
    assert r.residue_string == '15:3;2'

    r = Residue(15, 3, 2, ResidueModification('O-'))
    assert r.residue_string == 'O-15:3;2'

    r = Residue(15, 3, 2, ResidueModification('d'))
    assert r.residue_string == 'd15:3;2'

