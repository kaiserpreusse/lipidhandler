from lipidhandler.xref import Xref
from lipidhandler.xreflist import XrefList

def test_xreflist():

    xreflist = XrefList(
        [Xref('test', 'my_name'), Xref('swisslipids', 'SLM:000020715')]
    )

    assert len(xreflist) == 2

    # empty
    xreflist = XrefList()
    assert len(xreflist) == 0