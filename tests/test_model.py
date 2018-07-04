import sysml
import pytest
import uuid

# Notes: block elements with starting property attributes should be broken down into granular blocks and assigned id's & relationships upon assimilation into model.
@pytest.fixture
def model():
    """Create a model object that will also serve as the root directory for all other model elements"""
    model = sysml.Model('Constitution-Class Starship')
    return model

def test_model(model):
    assert repr(model) ==  "\xabmodel\xbb \nConstitution-Class Starship"
    assert repr(type(model)) ==  "<class 'sysml.system.Model'>"
    with pytest.raises(TypeError) as info:
        model = sysml.Model(47)
        assert "must be a string" in str(info.value)

"""Structure"""
# @pytest.mark.skip('WIP')
def test_package(model):
    """Create a package, labeled 'Structure', within model which will serve as namespace for the system structure

    Note: Model and Package objects can be thought of as a dict-like container for returning stereotyped model elements
    """
    with pytest.raises(TypeError) as info:
        model.add_package()
        assert "add_package() missing 1 required positional argument: 'name'" in str(info.value)
    with pytest.raises(KeyError) as info:
        model['holodeck']
        assert "holodeck" in str(info.value)
    model.add_package('Structure')
    assert repr(model['Structure']) == "\xabpackage\xbb \nStructure"
    assert repr(type(model['Structure'])) ==  "<class 'sysml.element.Package'>"
    assert uuid.UUID(model['Structure'].uuid, version=1)
    with pytest.raises(TypeError) as info:
        model['Structure'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block(model):
    """Add block elements to package objects using built-in add_block() method"""
    with pytest.raises(TypeError) as info:
        model['Structure'].add_block()
        assert "add_block() missing 1 required positional argument: 'name'" in str(info.value)
    model['Structure'].add_block('Constitution-class starship')
    assert repr(model['Structure']['Constitution-class starship']) == "\xabblock\xbb \nConstitution-class starship"
    assert repr(type(model['Structure']['Constitution-class starship'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].uuid, version=1)
    assert model['Structure']['Constitution-class starship'].multiplicity == 1
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty(model):
    """Add block elements as parts to parent blocks using add_part() method

    Parts added to a block element are dictionary-callable via the 'parts' attribute"""
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].add_part()
        assert "add_part() missing 1 required positional argument: 'name'" in str(info.value)
    model['Structure']['Constitution-class starship'].add_part('Primary Hull')
    model['Structure']['Constitution-class starship'].add_part('Engineering Hull')

    assert repr(model['Structure']['Constitution-class starship'].parts['Primary Hull']) == "\xabblock\xbb \nPrimary Hull"
    assert repr(model['Structure']['Constitution-class starship'].parts['Engineering Hull']) == "\xabblock\xbb \nEngineering Hull"

    assert repr(type(model['Structure']['Constitution-class starship'].parts['Primary Hull'])) ==  "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['Engineering Hull'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Primary Hull'].uuid, version=1)

    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Engineering Hull'].uuid, version=1)
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].parts['Primary Hull'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].parts['Primary Hull'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

    assert model['Structure']['Constitution-class starship'].parts['Primary Hull'].multiplicity == 1
    assert model['Structure']['Constitution-class starship'].parts['Engineering Hull'].multiplicity == 1
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].parts['Primary Hull'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].parts['Engineering Hull'].multiplicity = -1
        assert "must be a positive int" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty_withMultiplicity(model):
    """Add block elements as parts to parent blocks, with multiplicity, using add_part() method"""
    model['Structure']['Constitution-class starship'].add_part('Nacelle', multiplicity=2)
    model['Structure']['Constitution-class starship'].add_part('Pylon', multiplicity=2)
    assert repr(model['Structure']['Constitution-class starship'].parts['Nacelle']) == "\xabblock\xbb \nNacelle"
    assert repr(model['Structure']['Constitution-class starship'].parts['Pylon']) == "\xabblock\xbb \nPylon"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['Nacelle'])) == "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['Pylon'])) == "<class 'sysml.element.Block'>"
    assert model['Structure']['Constitution-class starship'].parts['Nacelle'].multiplicity == 2
    assert model['Structure']['Constitution-class starship'].parts['Pylon'].multiplicity == 2
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].parts['Pylon'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].parts['Pylon'].multiplicity = -1
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

@pytest.mark.skip('WIP')
def test_bdd(model):
    "Methods can also be called on package objects for generating 'diagram objects' for the 9 SysML diagrams"
    model['Structure'].bdd() # generates a block-definition diagram object on the 'Structure' package
    model['Structure'].show() # show diagrams generated for package, 'Structure'
    # Need some way to test diagram was generated

"""Analysis"""
@pytest.mark.skip('WIP')
def test_interaction(model):
    """Create an interaction, stereotyped as a test case, to be used to verify a requirement"""
    pass
    # model.add_package('Analysis')
    # model['Analysis'].add_interaction('Warp Field Analysis','testCase')

"""Requirements"""
# @pytest.mark.skip('WIP')
def test_requirements(model):
    """Create a package, labeled 'Requirements', within model which will serve as namespace for the system

    Define two requirement elements, passing in a string name and text field as its constructor arguments
    """
    model.add_package('Requirements') # creates a package, labeled 'Requirements', within model for storing model requirements
    with pytest.raises(TypeError) as info:
        model['Requirements'].add_requirement()
        assert "add_requirement() missing 2 required positional argument: 'name' and 'txt'" in str(info.value)
    model['Requirements'].add_requirement('Top-level', 'A constitution-class starship shall provide a 5-year mission capability to explore strange new worlds, to seek out new life and new civilizations, and to boldly go where no one has gone before.')
    model['Requirements'].add_requirement('Functional', 'A constitution-class starship shall be able to travel at warp 8 or higher')
    assert repr(model['Requirements']['Top-level']) == "\xabrequirement\xbb \nTop-level"
    assert repr(model['Requirements']['Functional']) == "\xabrequirement\xbb \nFunctional"
    assert repr(type(model['Requirements']['Top-level'])) ==  "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['Functional'])) ==  "<class 'sysml.element.Requirement'>"
    assert uuid.UUID(model['Requirements']['Top-level'].uuid, version=1)
    assert uuid.UUID(model['Requirements']['Functional'].uuid, version=1)
    with pytest.raises(TypeError) as info:
        model['Requirements']['Top-level'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Requirements']['Top-level'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

# @pytest.mark.skip('WIP')
def test_derive_requirement(model):
    """Define a dependency relationship, of stereotype «derive», between two requirements"""
    with pytest.raises(TypeError) as info:
        model['Requirements'].add_dependency()
        assert "add_dependency() missing 3 required positional arguments: 'source', 'target', and 'stereotype'" in str(info.value)
    model['Requirements'].add_dependency(model['Requirements']['Top-level'], model['Requirements']['Functional'], 'deriveReqt')
    assert repr(model['Requirements']['dependency1'].source) == "\xabrequirement\xbb \nTop-level"
    assert repr(model['Requirements']['dependency1'].target) == "\xabrequirement\xbb \nFunctional"
    assert repr(type(model['Requirements']['dependency1'])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements']['dependency1'].source)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency1'].target)) == "<class 'sysml.element.Requirement'>"
    assert model['Requirements']['dependency1'].stereotype == "deriveReqt"
    assert uuid.UUID(model['Requirements']['dependency1'].uuid, version=1)
    with pytest.raises(TypeError) as info:
        model['Requirements']['dependency1'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Requirements']['dependency1'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

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
    """Define a dependency relationship, of stereotype «satisfy», between a requirement and block"""
    model['Structure']['Constitution-class starship'].add_part('class-7 warp drive')
    model['Requirements'].add_dependency(model['Requirements']['Functional'], model['Structure']['Constitution-class starship'].parts['class-7 warp drive'], 'satisfy')
    assert repr(model['Requirements']['dependency2'].source) == "\xabrequirement\xbb \nFunctional"
    assert repr(model['Requirements']['dependency2'].target) == "\xabblock\xbb \nclass-7 warp drive"
    assert repr(type(model['Requirements']['dependency2'])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements']['dependency2'].source)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency2'].target)) == "<class 'sysml.element.Block'>"
    assert model['Requirements']['dependency2'].stereotype == "satisfy"
    assert uuid.UUID(model['Requirements']['dependency2'].uuid, version=1)
    with pytest.raises(TypeError) as info:
        model['Requirements']['dependency2'].uuid = 47
        assert "must be a valid uuid of type, string" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Requirements']['dependency2'].uuid = "47"
        assert "must be a valid uuid of type, string" in str(info.value)

@pytest.mark.skip('WIP')
def test_verify_requirement(model):
    pass
    # instantiate test case
    # add dependency where requirement is source node (i.e., "supplier") and test case is target node (i.e., "client")
    # assert dependency source is of type(Requirement)
    # assert dependency target stereotype is a «testCase»
    # assert dependency stereotype is "verify"


if __name__ == '__main__':
    print(__doc__)
    pytest.main(args=['-v'])
