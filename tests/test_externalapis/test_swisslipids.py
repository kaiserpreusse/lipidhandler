import pytest

from lipidhandler.lipid import Lipid
from lipidhandler.externalapis.swisslipids import SwissLipids


@pytest.mark.externalapi
def test_swisslipids_entity():
    sl = SwissLipids()

    lipid = sl.lipid_from_id('SLM:000020715')

    assert lipid.lipidclass.name == 'PC'
    assert len(lipid.residues) == 2
    assert lipid.residues[0].carbon_atoms == 28
    assert lipid.residues[0].double_bonds == 5
    assert lipid.residues[0].oxidation == None
    assert len(lipid.residues[0].zstatelist) == 5
    assert str(lipid.residues[0].zstatelist[1]) == '16Z'


@pytest.mark.externalapi
def test_swisslipids_search():
    sl = SwissLipids()

    lipidlist = sl.search('CE 20:2')

    for lipid in lipidlist:
        assert isinstance(lipid, Lipid)
        assert str(lipid.lipidclass) == 'CE'
