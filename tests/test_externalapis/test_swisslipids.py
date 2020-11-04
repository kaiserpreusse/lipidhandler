import pytest

from lipidhandler.lipid import Lipid
from lipidhandler.externalapis.swisslipids import SwissLipids


@pytest.mark.externalapi
def test_swisslipids_entity():

    lipid = SwissLipids.lipid_from_id('SLM:000020715')

    assert lipid.lipidclass.name == 'PC'
    assert len(lipid.residues) == 2
    assert lipid.residues[0].carbon_atoms == 28
    assert lipid.residues[0].double_bonds == 5
    assert lipid.residues[0].oxidation == None
    assert len(lipid.residues[0].zstatelist) == 5
    assert str(lipid.residues[0].zstatelist[1]) == '16Z'

@pytest.mark.externalapi
class TestSwissLipidsSearch:

    def test_search(self):

        lipidlist = SwissLipids.search('CE 20:2')

        for lipid in lipidlist:
            assert isinstance(lipid, Lipid)
            assert str(lipid.lipidclass) == 'CE'

    def test_search_no_result(self):
        empty_lipidlist = SwissLipids.search('klsdjghlzksfghj')
        assert len(empty_lipidlist) == 0


@pytest.mark.externalapi
def test_swisslipids_xref():
    lipid = Lipid.parse('CE(20:2)')

    lipid = SwissLipids.get_xrefs(lipid)

    for xref in lipid.xreflist:
        assert xref.target_db == SwissLipids.NAME

    assert any(x.target_id == 'SLM:000500283' for x in lipid.xreflist)
