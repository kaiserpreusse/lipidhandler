from lipidhandler.lipid import Lipid
from lipidhandler.residuelist import ResidueList
from lipidhandler.residue import Residue
from lipidhandler.lipidclass import LipidClass


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
