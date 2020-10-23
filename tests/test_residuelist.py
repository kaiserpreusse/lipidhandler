from lipidhandler.residuelist import ResidueList


def test_residuelist_parse():
    test_string = '18:1;0_19:1;0'

    residuelist = ResidueList.parse(test_string)

    assert len(residuelist) == 2

    assert residuelist[0].carbon_atoms == 18
    assert residuelist[0].double_bonds == 1
    assert residuelist[0].oxidation == 0

    assert residuelist[1].carbon_atoms == 19
    assert residuelist[1].double_bonds == 1
    assert residuelist[1].oxidation == 0

    test_string = '18:1_19:1'

    residuelist = ResidueList.parse(test_string)

    assert len(residuelist) == 2

    assert residuelist[0].carbon_atoms == 18
    assert residuelist[0].double_bonds == 1
    assert residuelist[0].oxidation == None

    assert residuelist[1].carbon_atoms == 19
    assert residuelist[1].double_bonds == 1
    assert residuelist[1].oxidation == None

    test_string = 'O-16:0;0/18:1;0'

    residuelist = ResidueList.parse(test_string)

    assert len(residuelist) == 2

    assert residuelist[0].carbon_atoms == 16
    assert residuelist[0].double_bonds == 0
    assert residuelist[0].oxidation == 0
    assert residuelist[0].olinked is True

    assert residuelist[1].carbon_atoms == 18
    assert residuelist[1].double_bonds == 1
    assert residuelist[1].oxidation == 0
    assert residuelist[1].olinked is False
