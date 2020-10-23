from __future__ import annotations
import logging

from lipidhandler.dictionaries import PREFERRED_CLASS

log = logging.getLogger(__name__)


class LipidClass:

    def __init__(self, name: str = None, input: str = None):
        self.name = name

        self.input = input

    @classmethod
    def parse(cls, string: str) -> LipidClass:
        """
        Parse an input string to extract the lipid class, map to preferred class name.

        :param string: Input String.
        :return: Instance of LipidClass
        """
        string = string.strip()

        if string in PREFERRED_CLASS:
            name = PREFERRED_CLASS[string]
        else:
            name = string

        return cls(name, string)
