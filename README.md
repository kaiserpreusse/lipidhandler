# Work with lipid names in Python

[![build](https://github.com/kaiserpreusse/lipidhandler/workflows/build/badge.svg)](https://github.com/kaiserpreusse/lipidhandler/actions?query=workflow%3Abuild)
[![PyPI](https://img.shields.io/pypi/v/lipidhandler)](https://pypi.org/project/lipidhandler)
![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue)
![PyPI - License](https://img.shields.io/pypi/l/lipidhandler)

LipidHandler is a Python package build to work with common abbreviations for lipids such as `CE(20:2)` or 
`PG(18:2/20:2)`. Those lipid names are used in publications, data reports and data analysis tools.

The main goal of LipidHandler is to **parse** those lipid names, provide facilities to **translate** 
them into other represantations and **map** them to official identifiers.

LipidHandler does not replace toolkits to work with molecules and chemical structures.

> :warning: LipidHandler was built for a specific research project and is not able to
> solve every use case about lipid names. It overlaps with other projects such as [liputils](https://github.com/Stemanz/liputils).


> :warning: The developer is not an expert on lipidomics, some of the naming might not make sense
> from a chemistry perspective.

> :mailbox: Feedback through GitHub issues is appreciated.

## install

`pip install lipidhandler`


## Getting started

### Work with lipid names
#### The Lipid class
Parse a lipid name:

```python
from lipidhandler import Lipid

mylipid = Lipid.parse('CE 20:2')
```

The `Lipid` has a `LipidClass`

```python
print(mylipid.lipidclass)

>>> CE
```

The `Lipid` contains a `ResidueList` which holds the `Residues`.

```python
# iterate the ResidueList
for residue in mylipid.residueslist:
    print(residue.carbon_atoms)
    print(residue.double_bonds)

>>> 20
>>> 0
```

Multiple residues and different formats are possible:

```python
mylipid = Lipid.parse("CE(20:2/18:2)")
mylipid = Lipid.parse("CE 20:2/18:2")
mylipid = Lipid.parse("CE(20:2_18:0)")
```
#### The Reside class
Next to the core attributes (C and double bonds) the `Residue` has an oxidation state, a generic
chemical modification descriptor and details on the isomer.

##### Oxidation state
```python
mylipid = Lipid.parse("CE(16:1;0)")
print(mylipid.residueslist[0].oxidation)

>>> 0
```
##### chemical modification

```python
mylipid = Lipid.parse("PE(O-16:1)")
print(mylipid.residueslist[0].modification)

>>> O-
```

##### isomer

```python
mylipid = Lipid.parse("CE(16:1(6Z))")
print(mylipid.residueslist[0].zstatelist[0]

>>> 6Z
```

The `ResidueList` has functions to aggregate over the residues:

```python
mylipid = Lipid.parse("CE(20:2/18:2)")
print(mylipid.residuelist.sum().carbon_atoms) # the .sum() functions returns a Residue instancte
```

### Connect to external databases
LipidHandler can query external sources to search for terms or get identifiers from external databases.
Right now LipidHandler only works with SwissLipids but the underliying interface is generic and
 can be extended. 

```python
from lipidhandler.externalapis import SwissLipids

lipids = SwissLipids.search("CE 20:2")
for l in lipids:
    print(l)

>>> CE(20:2)
```
The output of the `.search()` function is a `LipidList` which contains `Lipid` instances. If you 
search for more generic terms you get a list with multiple results.

```python
from lipidhandler.externalapis import SwissLipids

lipids = SwissLipids.search("CE 20")
for l in lipids:
    print(l)


>>> CE(20:1)
>>> CE(20:2)
>>> CE(20:5)
>>> CE(20:0)
>>> CE(20:4)
>>> CE(20:3)
>>> CE(20:4)
>>> CE(20:3)
```

You can also ask for the SwissLipds ID for a specific `Lipid` instance:

```python
from lipidhandler.externalapis import SwissLipids

mylipid = Lipid.parse("CE(20:2)")
db_xrefs = SwissLipids.get_xrefs(mylipid)
for xref in db_xrefs:
    print(xref.target_db, xref.target_id)

>>> SwissLipids SLM:00050028
```

## develop

### run tests
Install project and test dependencies

```shell script
pip install -r requirements.txt
pip install -r test_requirements.txt
```

Run test suite on sources

```shell script
python -m pytest
```
