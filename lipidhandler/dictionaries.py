from lipidhandler.residuemodification import ResidueModification
##############################################################
# A collection of mapping dictionaries
##############################################################



PREFERRED_CLASS = {
    'TAG': 'TG',
    'DAG': 'DG'
}

CLASS_DEFAULT_MODIFICATION = {
    'Cer': ResidueModification('d')
}