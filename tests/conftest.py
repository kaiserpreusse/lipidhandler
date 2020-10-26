import pytest
import random

from lipidhandler.residuelist import ResidueList
from lipidhandler.residue import Residue
from lipidhandler.residuemodification import ResidueModification
from lipidhandler.lipid import Lipid
from lipidhandler.lipidclass import LipidClass
from lipidhandler.lipidlist import LipidList


@pytest.fixture
def some_lipids_plain_list():
    """
    A handful of well formatted lipids, using all annotation elements.

    Return as Python list, not as LipidList Object
    """
    # lists of names to draw from
    lipidclass_names = ['CE', 'Cer', 'TG']
    modifications = ['d', 'O-', None, None]

    lipidlist = []

    for i in range(10):
        lipidclass = LipidClass(random.choice(lipidclass_names))

        num_of_residues = random.choice([1, 2, 3])

        residuelist = ResidueList()

        for i in range(0, num_of_residues):
            residuelist.residues.append(
                Residue(random.randint(6, 50), random.randint(0, 10), modification=ResidueModification(random.choice(modifications)))
            )

        lipidlist.append(
            Lipid(lipidclass, residuelist)
        )

    return lipidlist
