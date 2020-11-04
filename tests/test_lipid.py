import pytest

from lipidhandler.lipid import Lipid
from lipidhandler.residuelist import ResidueList
from lipidhandler.residue import Residue
from lipidhandler.lipidclass import LipidClass
from lipidhandler.residuemodification import ResidueModification
from lipidhandler.xref import Xref
from lipidhandler.dictionaries import CLASS_DEFAULT_MODIFICATION


class TestLipidParse:
    def test_parse(self):
        t = 'CE 16:2;0'
        lipid = Lipid.parse(t)
        assert lipid.lipidclass.name == 'CE'
        assert lipid.residues[0].carbon_atoms == 16
        assert lipid.residues[0].double_bonds == 2
        assert lipid.residues[0].oxidation == 0

        t = 'CE(16:2;0)'
        lipid = Lipid.parse(t)
        assert lipid.lipidclass.name == 'CE'
        assert lipid.residues[0].carbon_atoms == 16
        assert lipid.residues[0].double_bonds == 2
        assert lipid.residues[0].oxidation == 0

        t = 'DAG 16:0;0_22:4;0'
        lipid = Lipid.parse(t)
        assert lipid.lipidclass.name == 'DG'
        assert len(lipid.residues) == 2
        assert lipid.residues[0].carbon_atoms == 16
        assert lipid.residues[0].double_bonds == 0
        assert lipid.residues[0].oxidation == 0

        t = 'PC(28:5(13Z,16Z,19Z,22Z,25Z)/0:0)'
        lipid = Lipid.parse(t)
        assert lipid.lipidclass.name == 'PC'
        assert len(lipid.residues) == 2
        assert lipid.residues[0].carbon_atoms == 28
        assert lipid.residues[0].double_bonds == 5
        assert lipid.residues[0].oxidation == None
        assert len(lipid.residues[0].zstatelist) == 5
        assert str(lipid.residues[0].zstatelist[1]) == '16Z'

        t = 'chol'
        lipid = Lipid.parse(t)
        assert str(lipid.lipidclass) == 'chol'


    def test_errors(self):
        with pytest.raises(TypeError):
            # string not ending with bracket
            Lipid.parse("CE(14:9(9Z)/8:0")


def test_lipid_xreflist():
    t = 'DAG 16:0;0_22:4;0'
    lipid = Lipid.parse(t)

    lipid.add_xref(
        Xref('TargetDB', 'targetid')
    )
    assert len(lipid.xreflist) == 1


def test_lipid_abbreviation():
    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2)]))

    assert l.abbreviation() == 'CE(16:2)'

    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2), Residue(18, 1)]))

    assert l.abbreviation() == 'CE(16:2/18:1)'
    assert l.abbreviation(summed=True) == 'CE(34:3)'

    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2, modification=ResidueModification('O-')), Residue(18, 1)]))

    assert l.abbreviation() == 'CE(O-16:2/18:1)'
    assert l.abbreviation(summed=True) == 'CE(O-34:3)'

    # no residues, assure that abbreviation/summed fails with AttributeError
    l = Lipid(LipidClass('CE'))
    assert l.abbreviation() == 'CE'

    assert l.abbreviation(summed=True) == 'CE'


def test_lipid_check_consistency():
    l = Lipid(LipidClass('Cer'), ResidueList([Residue(16, 2), Residue(18, 1)]))

    # check inconsistent state
    assert l.residues[0].modification == None

    l.check_consistency()

    # check consistent state
    assert l.residues[0].modification == CLASS_DEFAULT_MODIFICATION['Cer']
