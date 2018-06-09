import sysml
import pytest
import uuid

"""Structure"""
# Notes: block elements with starting property attributes should be broken down into granular blocks and assigned id's & relationships upon assimilation into model.
@pytest.fixture
def model():
    "Create a SysML model instance"
    model = sysml.Model('Constitution-Class Starship')
    return model

def test_model(model):
    assert repr(model) ==  "\xabmodel\xbb 'Constitution-Class Starship'"
    assert repr(type(model)) ==  "<class 'sysml.system.Model'>"

# @pytest.mark.skip('WIP')
def test_add_package(model):
    model.add_package('Structure')
    assert repr(model['Structure']) == "\xabpackage\xbb 'Structure'"
    assert repr(type(model['Structure'])) ==  "<class 'sysml.element.Package'>"
    assert uuid.UUID(model['Structure'].uuid, version=1)

# @pytest.mark.skip('WIP')
def test_add_block_to_package(model):
    """ add block elements as parts to parent blocks using `add_block` the method"""
    model['Structure'].add_block('Constitution-class starship')
    assert repr(model['Structure']['Constitution-class starship']) == "\xabblock\xbb 'Constitution-class starship'"
    assert repr(type(model['Structure']['Constitution-class starship'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].uuid, version=1)

# @pytest.mark.skip('WIP')
def test_add_parts_to_block(model):
    "Parts added to a block element are callable by index via the 'parts' attribute"
    model['Structure']['Constitution-class starship'].add_part('Primary Hull')
    model['Structure']['Constitution-class starship'].add_part('Engineering Hull')
    assert repr(model['Structure']['Constitution-class starship'].parts['Primary Hull']) == "\xabblock\xbb 'Primary Hull'"
    assert repr(model['Structure']['Constitution-class starship'].parts['Engineering Hull']) == "\xabblock\xbb 'Engineering Hull'"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['Primary Hull'])) ==  "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['Engineering Hull'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Primary Hull'].uuid, version=1)
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Engineering Hull'].uuid, version=1)

@pytest.mark.skip('WIP')
def test_bdd(model):
    "methods can also be called on package objects for generating 'diagram objects' for the 9 SysML diagrams"
    model = add_parts_to_block
    model['Structure'].bdd() # generates a block-definition diagram object on the 'Structure' package
    model['Structure'].show() # show diagrams generated for package, 'Structure'
    # Need some way to test diagram was generated

@pytest.mark.skip('WIP')
def test_create_model_instance(model):
    ncc1701 = create_instance
    ncc1701.label = 'NCC-1701'
    assert repr(model) == "\xabmodel\xbb 'Constitution-Class Starship'"
    assert repr(ncc1701) == "\xabmodel\xbb 'NCC-1701'"

"""Requirements"""
# @pytest.mark.skip('WIP')
def test_add_requirements(model):
    model.add_package('Requirements') # creates a package, labeled 'Requirements', within model for storing model requirements
    model['Requirements'].add_requirement('Top-level', 'A constitution-class starship shall provide a 5-year mission capability to explore strange new worlds, to seek out new life and new civilizations, and to boldly go where no one has gone before.')
    model['Requirements'].add_requirement('Functional', 'A constitution-class starship shall be able to travel at warp 8 or higher')
    assert repr(model['Requirements']['Top-level']) == "\xabrequirement\xbb 'Top-level'"
    assert repr(model['Requirements']['Functional']) == "\xabrequirement\xbb 'Functional'"
    assert repr(type(model['Requirements']['Top-level'])) ==  "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['Functional'])) ==  "<class 'sysml.element.Requirement'>"
    assert uuid.UUID(model['Requirements']['Top-level'].uuid, version=1)
    assert uuid.UUID(model['Requirements']['Functional'].uuid, version=1)

# @pytest.mark.skip('WIP')
def test_derive_requirement(model):
    model['Requirements'].add_dependency(model['Requirements']['Top-level'], model['Requirements']['Functional'], 'deriveReqt')
    assert repr(model['Requirements']['dependency1'].source) == "\xabrequirement\xbb 'Top-level'"
    assert repr(model['Requirements']['dependency1'].target) == "\xabrequirement\xbb 'Functional'"
    assert repr(type(model['Requirements']['dependency1'].source)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency1'].target)) == "<class 'sysml.element.Requirement'>"
    assert model['Requirements']['dependency1'].stereotype == "deriveReqt"
    assert uuid.UUID(model['Requirements']['dependency1'].uuid, version=1)

@pytest.mark.skip('WIP')
def test_refine_requirement(model):
    pass
    # instantiate use case
    # add dependency where requirement is source node (i.e., "supplier") and use case is target node (i.e., "client")
    # assert dependency source is of type(requirement)
    # assert dependency target is of type(use case)
    # assert dependency stereotype is "refine"

# @pytest.mark.skip('WIP')
def test_satisfy_requirement(model):
    model['Structure']['Constitution-class starship'].add_part('class-7 warp drive')
    model['Requirements'].add_dependency(model['Requirements']['Functional'], model['Structure']['Constitution-class starship'].parts['class-7 warp drive'], 'satisfy')
    assert repr(model['Requirements']['dependency2'].source) == "\xabrequirement\xbb 'Functional'"
    assert repr(model['Requirements']['dependency2'].target) == "\xabblock\xbb 'class-7 warp drive'"
    assert repr(type(model['Requirements']['dependency2'].source)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency2'].target)) == "<class 'sysml.element.Block'>"
    assert model['Requirements']['dependency2'].stereotype == "satisfy"
    assert uuid.UUID(model['Requirements']['dependency2'].uuid, version=1)

@pytest.mark.skip('WIP')
def test_verify_requirement(model):
    pass
    # instantiate test case
    # add dependency where requirement is source node (i.e., "supplier") and test case is target node (i.e., "client")
    # assert dependency source is of type(Requirement)
    # assert dependency target stereotype is a «testCase»
    # assert dependency stereotype is "verify"
