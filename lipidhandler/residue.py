from __future__ import annotations
import logging

log = logging.getLogger(__name__)


class Residue:

    def __init__(self, carbon_atoms: int = None, double_bonds: int = None, oxidation: int = None,
                 olinked: bool = False):
        self.carbon_atoms = carbon_atoms
        self.double_bonds = double_bonds
        self.oxidation = oxidation
        self.olinked = olinked

    @classmethod
    def parse(cls, string: str) -> Residue:
        """
        Parse a string to create Residue. This will fail if a string with more than one residue is
        passed, the ResidueList is the default entrypoint.

        :param string:
        :return:
        """

        olinked = False
        if string.strip().startswith('O-'):
            olinked = True
            string = string.replace('O-', '')

        log.debug(string)
        chain_def = string.split(';')[0]
        carbon_atoms, double_bonds = chain_def.split(':')

        if ';' in string:
            oxidation = int(string.split(';')[1])
        else:
            oxidation = None

        return cls(int(carbon_atoms), int(double_bonds), oxidation, olinked)
