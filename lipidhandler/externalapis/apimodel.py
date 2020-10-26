import logging

from lipidhandler.lipidlist import LipidList

log = logging.getLogger(__name__)


class ExternalApi:

    def __init__(self):
        pass

    def search(self, search_term) -> LipidList:
        raise NotImplementedError