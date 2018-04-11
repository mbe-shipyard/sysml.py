from sysmlpy import sysml
import pytest

@pytest.fixture
def test_import_yaml():
    "Import model by specifying yaml file"
    model = sysml.import_yaml('firesat.yaml')
    return model

def test_elements(model):
    "Display model elements (as a list of key value pairs?)"
    model.elements
    #assert repr(model.elements) ==

def test_elements(model):
    "Display model relationships (as a list of key value pairs?)"
    model.relationships
    #assert repr(model.relationships) ==

def test_bdd(model):
    "Generate a BlockDefinitionDiagram by specifying package label"
    bdd = model.bdd('FireSat Mission Requirements') # pass in package label for the BlockDefinitionDiagram to be generated
    #assert repr(bdd) ==

def test_req(model):
    "Generate RequirementDiagram by specifying package label"
    req = model.req('FireSat Mission Requirements') # pass in package label for the BlockDefinitionDiagram to be generated
    #assert repr(req) ==

def test_par(model):
    "Generate a BlockDefinitionDiagram by specifying package label"
    bdd = model.bdd('FireSat Mission Requirements') # pass in package label for the BlockDefinitionDiagram to be generated
    #assert repr(bdd) ==
