from lipidhandler.lipid import Lipid
from lipidhandler.residuelist import Residue
from lipidhandler.lipidlist import LipidList


def test_lipidlist_iter(some_lipids_plain_list):

    lipidlist = LipidList(some_lipids_plain_list)

    assert len(lipidlist) == len(some_lipids_plain_list)
    for l in lipidlist:
        assert isinstance(l, Lipid)


def test_lipidlist_append():
    lipidlist = LipidList()

    for i in range(10):
        lipidlist.append(
            Lipid()
        )

    assert len(lipidlist) == 10
