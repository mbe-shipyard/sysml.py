import sysml
import pytest
import uuid

# Notes:
# block elements with starting property attributes should be broken down into granular blocks and assigned id's & relationships upon assimilation into model.
# Need to add tests for ensuring mutable default arguments

@pytest.fixture(scope="module")
def model():
    """Create a model object that will also serve as the root directory for all other model elements"""
    model = sysml.Model('Constitution-class Starship')
    return model

def test_model(model):
    assert repr(model) ==  "\xabmodel\xbb\nConstitution-class Starship"
    assert repr(type(model)) ==  "<class 'sysml.system.Model'>"

    assert model.stereotype == ['model']

    with pytest.raises(TypeError) as info:
        model = sysml.Model(47)
        assert "must be a string" in str(info.value)
    with pytest.raises(TypeError) as info:
        model = sysml.ModelElement()
        assert "Can't instantiate abstract class base with abstract methods" in str(info.value)

"""Structure"""
# @pytest.mark.skip('WIP')
def test_package(model):
    """Create a package, labeled 'Structure', within model which will serve as namespace for the system structure

    Note: Model and Package objects can be thought of as a dict-like container for returning stereotyped model elements
    """

    with pytest.raises(TypeError) as info:
        model.add()
        assert "add() missing 1 required positional argument: 'name'" in str(info.value)

    holodeck = sysml.Package('Holodeck')

    assert holodeck.stereotype == ['package']

    model.add(holodeck)

    assert repr(model['Holodeck']) == "\xabpackage\xbb\nHolodeck"
    assert repr(type(model['Holodeck'])) ==  "<class 'sysml.element.Package'>"
    assert uuid.UUID(model['Holodeck'].uuid, version=1)

    model.remove(model['Holodeck'])

    with pytest.raises(KeyError) as info:
        model['Holodeck']
        assert "Holodeck" in str(info.value)

    model.add(sysml.Package('Structure'))

    assert repr(model['Structure']) == "\xabpackage\xbb\nStructure"
    assert repr(type(model['Structure'])) ==  "<class 'sysml.element.Package'>"
    assert uuid.UUID(model['Structure'].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['Structure'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Structure'].uuid = "47"
        assert "can't set attribute" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block(model):
    """Add block elements to package objects using built-in add_part() method"""

    with pytest.raises(TypeError) as info:
        model['Structure'].add()
        assert "add() missing 1 required positional argument: 'name'" in str(info.value)

    model['Structure'].add(sysml.Block('Constitution-class Starship'))
    starship_block = model['Structure']['Constitution-class Starship']

    assert repr(model['Structure']['Constitution-class Starship']) == "\xabblock\xbb\nConstitution-class Starship"
    assert repr(type(model['Structure']['Constitution-class Starship'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class Starship'].uuid, version=1)
    assert model['Structure']['Constitution-class Starship'].multiplicity == 1

    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class Starship'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class Starship'].uuid = "47"
        assert "can't set attribute" in str(info.value)

def test_block_stereotype():
    """Test block stereotype"""
    enterprise = sysml.Block('NCC-1701',stereotype='constitutionClass')
    enterpriseD = sysml.Block('NCC-1701-D',stereotype=['galaxyClass','flagship'])

    assert enterprise.stereotype == ['block', 'constitutionClass']
    assert enterpriseD.stereotype == ['block', 'galaxyClass', 'flagship']

    with pytest.raises(TypeError) as info:
        enterpriseD = sysml.Block('NCC-1701-D',stereotype=47)
        assert "must be a string or set of strings" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty(model):
    """Add block elements as parts to parent blocks using add_part() method

    Parts added to a block element are dictionary-callable via the 'parts' attribute"""

    starship_block = model['Structure']['Constitution-class Starship']

    starship_block.add_part(sysml.Block('Primary Hull'))
    starship_block.add_part(sysml.Block('Engineering Hull'))
    starship_block.add_part(sysml.Block('Cloaking device'))

    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class Starship'].add_part()
        assert "add_part() missing 1 required positional argument: 'name'" in str(info.value)

    cloaking_device = starship_block.parts['Cloaking device']

    assert repr(model['Structure']['Constitution-class Starship'].parts['Primary Hull']) == "\xabblock\xbb\nPrimary Hull"
    assert repr(model['Structure']['Constitution-class Starship'].parts['Engineering Hull']) == "\xabblock\xbb\nEngineering Hull"
    assert repr(model['Structure']['Constitution-class Starship'].parts['Cloaking device']) == "\xabblock\xbb\nCloaking device"

    assert repr(type(model['Structure']['Constitution-class Starship'].parts['Primary Hull'])) ==  "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class Starship'].parts['Engineering Hull'])) ==  "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class Starship'].parts['Cloaking device'])) ==  "<class 'sysml.element.Block'>"

    assert uuid.UUID(model['Structure']['Constitution-class Starship'].parts['Primary Hull'].uuid, version=1)
    assert uuid.UUID(model['Structure']['Constitution-class Starship'].parts['Engineering Hull'].uuid, version=1)

    starship_block.remove_part(cloaking_device)

    with pytest.raises(KeyError) as info:
        model['Cloaking device']
        assert 'Cloaking device' in str(info.value)

    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class Starship'].parts['Primary Hull'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class Starship'].parts['Primary Hull'].uuid = "47"
        assert "can't set attribute" in str(info.value)

    assert model['Structure']['Constitution-class Starship'].parts['Primary Hull'].multiplicity == 1
    assert model['Structure']['Constitution-class Starship'].parts['Engineering Hull'].multiplicity == 1

    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class Starship'].parts['Primary Hull'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class Starship'].parts['Engineering Hull'].multiplicity = -1
        assert "must be a positive int" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty_withMultiplicity(model):
    """Add block elements as parts to parent blocks, with multiplicity, using add_part() method"""
    # notes: need to redesign multiplicity constructor and setter

    starship_block = model['Structure']['Constitution-class Starship']

    starship_block.add_part(sysml.Block('Nacelle', multiplicity=2))
    starship_block.add_part(sysml.Block('Pylon', multiplicity=2))

    assert repr(model['Structure']['Constitution-class Starship'].parts['Nacelle']) == "\xabblock\xbb\nNacelle"
    assert repr(model['Structure']['Constitution-class Starship'].parts['Pylon']) == "\xabblock\xbb\nPylon"

    assert repr(type(model['Structure']['Constitution-class Starship'].parts['Nacelle'])) == "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class Starship'].parts['Pylon'])) == "<class 'sysml.element.Block'>"

    assert model['Structure']['Constitution-class Starship'].parts['Nacelle'].multiplicity == 2
    assert model['Structure']['Constitution-class Starship'].parts['Pylon'].multiplicity == 2

    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class Starship'].parts['Pylon'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class Starship'].parts['Pylon'].multiplicity = -1
        assert "must be a positive int" in str(info.value)

@pytest.mark.skip('WIP')
def test_block_valueProperty(model):
    pass

@pytest.mark.skip('WIP')
def test_block_referenceProperty(model):
    pass

@pytest.mark.skip('WIP')
def test_block_constraintProperty(model):
    pass

@pytest.mark.skip('WIP')
def test_block_port(model):
    pass

"""Analysis"""
@pytest.mark.skip('WIP')
def test_interaction(model):
    """Create an interaction, stereotyped as a test case, to be used to verify a requirement"""
    pass
    # model.add(sysml.Package('Analysis'))
    # model['Analysis'].add(sysml.Interaction('Warp Field Analysis','testCase'))

"""Requirements"""
# @pytest.mark.skip('WIP')
def test_requirements(model):
    """Create a package, labeled 'Requirements', within model which will serve as namespace for the system

    Define two requirement elements, passing in a string name and text field as its constructor arguments
    """

    model.add(sysml.Package('Requirements')) # creates a package, labeled 'Requirements', within model for storing model requirements

    assert repr(model['Requirements']) == "\xabpackage\xbb\nRequirements"
    assert repr(type(model['Requirements'])) ==  "<class 'sysml.element.Package'>"

    assert uuid.UUID(model['Requirements'].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['Requirements'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements'].uuid = "47"
        assert "can't set attribute" in str(info.value)

    # with pytest.raises(TypeError) as info:
    #     model['Requirements'].add(sysml.Requirement())
    #     assert "Requirement() missing 2 required positional argument: 'name' and 'txt'" in str(info.value)

    model['Requirements'].add(sysml.Requirement('Top-level', 'A constitution-class starship shall provide a 5-year mission capability to explore strange new worlds, to seek out new life and new civilizations, and to boldly go where no one has gone before.'))
    model['Requirements'].add(sysml.Requirement('Functional', 'A constitution-class starship shall be able to travel at warp 8 or higher'))

    assert repr(model['Requirements']['Top-level']) == "\xabrequirement\xbb\nTop-level"
    assert repr(model['Requirements']['Functional']) == "\xabrequirement\xbb\nFunctional"

    assert repr(type(model['Requirements']['Top-level'])) ==  "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['Functional'])) ==  "<class 'sysml.element.Requirement'>"

    assert model['Requirements']['Top-level'].stereotype == ['requirement']

    assert uuid.UUID(model['Requirements']['Top-level'].uuid, version=1)
    assert uuid.UUID(model['Requirements']['Functional'].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['Requirements']['Top-level'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements']['Top-level'].uuid = "47"
        assert "can't set attribute" in str(info.value)

# @pytest.mark.skip('WIP')
def test_derive_requirement(model):
    """Define a dependency relationship, of stereotype «derive», between two requirements"""

    with pytest.raises(TypeError) as info:
        model['Requirements'].add(sysml.Dependency())
        assert "Dependency() missing 3 required positional arguments: 'supplier', 'client', and 'stereotype'" in str(info.value)

    supplier = model['Requirements']['Functional']
    client = model['Requirements']['Top-level']
    deriveReqt_dependency = sysml.Dependency(supplier, client, 'deriveReqt')
    model['Requirements'].add(deriveReqt_dependency)

    assert repr(model['Requirements'][deriveReqt_dependency.name].supplier) == "\xabrequirement\xbb\nFunctional"
    assert repr(model['Requirements'][deriveReqt_dependency.name].client) == "\xabrequirement\xbb\nTop-level"

    assert repr(type(model['Requirements'][deriveReqt_dependency.name])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements'][deriveReqt_dependency.name].supplier)) == "<class 'sysml.element.Requirement'>"

    assert repr(type(model['Requirements'][deriveReqt_dependency.name].client)) == "<class 'sysml.element.Requirement'>"
    assert model['Requirements'][deriveReqt_dependency.name].stereotype == "deriveReqt"

    assert uuid.UUID(model['Requirements'][deriveReqt_dependency.name].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['Requirements'][deriveReqt_dependency.name].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements'][deriveReqt_dependency.name].uuid = "47"
        assert "can't set attribute" in str(info.value)

@pytest.mark.skip('WIP')
def test_refine_requirement(model):
    pass
    # instantiate use case
    # add dependency where requirement is supplier node (i.e., "supplier") and use case is client node (i.e., "client")
    # assert dependency supplier is of type(requirement)
    # assert dependency client is of type(use case)
    # assert dependency stereotype is "refine"

# @pytest.mark.skip('WIP')
def test_satisfy_requirement(model):
    """Define a dependency relationship, of stereotype «satisfy», between a requirement and block"""

    starship_block = model['Structure']['Constitution-class Starship']

    warpdrive = sysml.Block('Class-7 Warp Drive')
    starship_block.add_part(warpdrive)

    reqt1 = model['Requirements']['Functional']
    satisfy_dependency = sysml.Dependency(warpdrive, reqt1, 'satisfy')
    model['Requirements'].add(satisfy_dependency)

    assert repr(warpdrive) == "\xabblock\xbb\nClass-7 Warp Drive"
    assert repr(reqt1) == "\xabrequirement\xbb\nFunctional"

    assert satisfy_dependency.stereotype == "satisfy"

    assert model['Requirements'][satisfy_dependency.name].name == satisfy_dependency.name
    assert model['Requirements'][satisfy_dependency.name].stereotype == "satisfy"

    assert repr(model['Requirements'][satisfy_dependency.name].supplier) == "\xabblock\xbb\nClass-7 Warp Drive"
    assert repr(model['Requirements'][satisfy_dependency.name].client) == "\xabrequirement\xbb\nFunctional"

    assert repr(type(model['Requirements'][satisfy_dependency.name])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements'][satisfy_dependency.name].supplier)) == "<class 'sysml.element.Block'>"
    assert repr(type(model['Requirements'][satisfy_dependency.name].client)) == "<class 'sysml.element.Requirement'>"

    assert uuid.UUID(model['Requirements'][satisfy_dependency.name].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['Requirements'][satisfy_dependency.name].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements'][satisfy_dependency.name].uuid = "47"
        assert "can't set attribute" in str(info.value)

@pytest.mark.skip('WIP')
def test_verify_requirement(model):
    pass
    # instantiate test case
    # add dependency where requirement is supplier node (i.e., "supplier") and test case is client node (i.e., "client")
    # assert dependency supplier is of type(Requirement)
    # assert dependency client stereotype is a «testCase»
    # assert dependency stereotype is "verify"


if __name__ == '__main__':
    print(__doc__)
    pytest.main(args=['-v'])
