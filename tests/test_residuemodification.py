from lipidhandler.residuemodification import ResidueModification


def test_eq():

    r1 = ResidueModification('a')
    r2 = ResidueModification('a')
    r3 = ResidueModification('b')

    assert r1 == r2
    assert r1 != r3
    assert r2 != r3
    assert 4 != r1
    assert r1 != 4
    assert r1 != None
    assert None != r1