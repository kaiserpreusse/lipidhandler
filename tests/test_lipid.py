from lipidhandler.lipid import Lipid
from lipidhandler.residuelist import ResidueList
from lipidhandler.residue import Residue
from lipidhandler.lipidclass import LipidClass
from lipidhandler.residuemodification import ResidueModification
from lipidhandler.dictionaries import CLASS_DEFAULT_MODIFICATION


def test_lipid_parse():
    t = 'CE 16:2;0'

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


def test_lipid_swisslipids_abbreviation():
    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2)]))

    assert l.swisslipids_abbreviation() == 'CE(16:2)'

    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2), Residue(18, 1)]))

    assert l.swisslipids_abbreviation() == 'CE(16:2/18:1)'
    assert l.swisslipids_abbreviation(summed=True) == 'CE(34:3)'

    l = Lipid(LipidClass('CE'), ResidueList([Residue(16, 2, modification=ResidueModification('O-')), Residue(18, 1)]))

    assert l.swisslipids_abbreviation() == 'CE(O-16:2/18:1)'
    assert l.swisslipids_abbreviation(summed=True) == 'CE(O-34:3)'


def test_lipid_check_consistency():
    l = Lipid(LipidClass('Cer'), ResidueList([Residue(16, 2), Residue(18, 1)]))

    # check inconsistent state
    assert l.residues[0].modification == None

    l.check_consistency()

    # check consistent state
    assert l.residues[0].modification == CLASS_DEFAULT_MODIFICATION['Cer']
