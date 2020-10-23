from __future__ import annotations
import logging

from lipidhandler.residuelist import ResidueList
from lipidhandler.lipidclass import LipidClass
from lipidhandler.residue import Residue

log = logging.getLogger(__name__)


class Lipid:

    def __init__(self, lipidclass: LipidClass = None, residues: ResidueList = None):
        self.residues = residues
        self.lipidclass = lipidclass
        self._input = None

    def swisslipids_abbreviation(self, summed: bool = False) -> str:
        """
        Return the abbreviation of the lipid in the format preferred by SwissLipids.

        E.g. CE(16:3)

        You can either return the summed residues or multiple residues.

        :arg summed: Summed or multiple residues.
        :return: SwissLipids abbreviation of the lipid.
        """
        if summed:
            return f'{self.lipidclass.name}({self.residue_sum().residue_string})'
        else:
            return f"{self.lipidclass.name}({self.residues.residuelist_string})"

    def residue_sum(self) -> Residue:
        """
        Sum up all carbon atoms and double bonds of all residues and return the sum.
        """
        return self.residues.sum()

    @classmethod
    def parse(cls, string: str) -> Lipid:
        """
        Parse a string represntation of a lipid and create Lipid class.

        :param string: The input string.
        :return: An instance of Lipid
        """
        if string.count('(') > 1 or string.count(')') > 1:
            raise NotImplementedError('alternative chains not implemented')


        # identify abbreviation type
        if '(' in string and ')' in string:
            pass

        # CE 22:4;0
        elif ' ' in string:
            lipid_class_name, residue_string = string.split(' ', 1)

            lipidclass = LipidClass.parse(lipid_class_name)
            residuelist = ResidueList.parse(residue_string)

            lipid = cls(lipidclass, residuelist)
            lipid._input = string
            return lipid


