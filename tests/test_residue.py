from lipidhandler.residue import Residue
from lipidhandler.residuemodification import ResidueModification


def test_residue_parse():
    r = Residue.parse("15:3")
    assert r.carbon_atoms == 15

    r = Residue.parse("d15:3")
    assert r.carbon_atoms == 15
    assert str(r.modification) == 'd'

    r = Residue.parse("15:3(6Z)")
    assert r.carbon_atoms == 15
    assert len(r.zstatelist) == 1
    assert str(r.zstatelist[0]) == '6Z'


def test_residue_string():
    r = Residue(15, 3)
    assert r.residue_string == "15:3"

    r = Residue(15, 3, 2)
    assert r.residue_string == '15:3;2'

    r = Residue(15, 3, 2, ResidueModification('O-'))
    assert r.residue_string == 'O-15:3;2'

    r = Residue(15, 3, 2, ResidueModification('d'))
    assert r.residue_string == 'd15:3;2'
