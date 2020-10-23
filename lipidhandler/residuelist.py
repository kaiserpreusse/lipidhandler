from __future__ import annotations
import logging

from lipidhandler.residue import Residue

log = logging.getLogger(__name__)


class ResidueList:

    def __init__(self, residues: list[Residue] = None):
        self.residues = residues

    def __len__(self):
        return len(self.residues)

    def __getitem__(self, item):
        return self.residues[item]

    def __iter__(self):
        return iter(self.residues)

    @classmethod
    def parse(cls, string: str) -> ResidueList:
        """
        Parse a string and return a list of Residues.

        :param string: Input string.
        :return: ResidueList instance.
        """
        # remove brackets
        log.debug(f'Parse input: {string}')

        if string.count('(') > 1 or string.count(')') > 1:
            raise NotImplementedError('alternative chains not implemented')

        if '(' in string and ')' in string:
            string = string.replace('(', '').replace(')', '')

        # check for residue splitter
        splittable = False
        split_char = None

        if '/' in string:
            splittable = True
            split_char = '/'
        elif '_' in string:
            splittable = True
            split_char = '_'

        residues = []
        residue_string_list = string.split(split_char)

        for residue_string in residue_string_list:
            residues.append(
                Residue.parse(residue_string)
            )

        return cls(residues)




