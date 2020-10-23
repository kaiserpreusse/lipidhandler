from __future__ import annotations
import logging

from lipidhandler.residuelist import ResidueList
from lipidhandler.lipidclass import LipidClass

log = logging.getLogger(__name__)


class Lipid:

    def __init__(self, lipidclass: LipidClass = None, residues: ResidueList = None):
        self.residues = residues
        self.lipidclass = lipidclass

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

            return cls(lipidclass, residuelist)


