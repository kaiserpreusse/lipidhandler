import requests
import logging

from lipidhandler.lipidlist import LipidList
from lipidhandler.lipid import Lipid
from lipidhandler.xref import Xref
from lipidhandler.externalapis.apimodel import ExternalApi

log = logging.getLogger(__name__)


class SwissLipids(ExternalApi):
    NAME = 'SwissLipids'
    BASE_URL = 'https://www.swisslipids.org/api/index.php'

    def __init__(self):
        super(SwissLipids, self).__init__()

    def search(self, search_term: str) -> LipidList:
        lipidlist = LipidList()

        for entity in self.run_search(search_term):
            swisslipidsid = entity['entity_id']
            lipidlist.append(
                self.lipid_from_id(swisslipidsid)
            )

        return lipidlist

    def get_xrefs(self, lipid: Lipid, summed: bool = False) -> Lipid:

        for entity in self.run_search(lipid.abbreviation(summed)):
            lipid.add_xref(Xref(self.NAME, entity['entity_id']))

        return lipid

    def lipid_from_id(self, swisslipidsid: str) -> Lipid:
        """
        Call API to get details for a SwissLipids ID.

        :param swisslipidsid: The SwissLipids ID.
        :return: Return a Lipid.
        """
        request_url = self.BASE_URL + f'/entity/{swisslipidsid.strip()}'
        log.debug(f'Call: {request_url}')

        result = requests.get(request_url).json()

        # get abbreviation
        for synonym in result['synonyms']:
            if synonym['type'] == 'abbreviation':
                abbreviation = synonym['name']

                lipid = Lipid.parse(abbreviation)
                lipid.add_xref(Xref(self.NAME, swisslipidsid))
                return lipid

    def run_search(self, search_term: str) -> dict:
        """
        Run a search against the SwissLipids API and return JSON result.

        :param search_term: The search term.
        :return: Result as JSON
        """
        request_url = self.BASE_URL + f'/search?term={search_term}'
        log.debug(f"Request URL: {request_url}")

        result = requests.get(request_url).json()

        return result

