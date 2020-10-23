from lipidhandler.lipidclass import LipidClass


def test_lipidclass_preferred_class_mapping():
    assert LipidClass.parse('TAG').name == 'TG'
    assert LipidClass.parse('DAG').name == 'DG'
