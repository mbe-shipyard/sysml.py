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
        model.new_package()
        assert "new_package() missing 1 required positional argument: 'name'" in str(info.value)
    with pytest.raises(KeyError) as info:
        model['holodeck']
        assert "holodeck" in str(info.value)
    model.new_package('Structure')
    assert repr(model['Structure']) == "\xabpackage\xbb \nStructure"
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
    """Add block elements to package objects using built-in new_block() method"""
    # with pytest.raises(TypeError) as info:
    #     model['Structure'].new_block()
    #     assert "new_block() missing 1 required positional argument: 'name'" in str(info.value)
    model['Structure'].new_block('Constitution-class starship')
    assert repr(model['Structure']['Constitution-class starship']) == "\xabblock\xbb \nConstitution-class starship"
    assert repr(type(model['Structure']['Constitution-class starship'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].uuid, version=1)
    assert model['Structure']['Constitution-class starship'].multiplicity == 1
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class starship'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class starship'].uuid = "47"
        assert "can't set attribute" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty(model):
    """Add block elements as parts to parent blocks using new_part() method

    Parts added to a block element are dictionary-callable via the 'parts' attribute"""
    # with pytest.raises(TypeError) as info:
    #     model['Structure']['Constitution-class starship'].new_part()
    #     assert "new_part() missing 1 required positional argument: 'name'" in str(info.value)
    model['Structure']['Constitution-class starship'].new_part('Primary Hull')
    model['Structure']['Constitution-class starship'].new_part('Engineering Hull')

    assert repr(model['Structure']['Constitution-class starship'].parts['primaryHull']) == "\xabblock\xbb \nPrimary Hull"
    assert repr(model['Structure']['Constitution-class starship'].parts['engineeringHull']) == "\xabblock\xbb \nEngineering Hull"

    assert repr(type(model['Structure']['Constitution-class starship'].parts['primaryHull'])) ==  "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['engineeringHull'])) ==  "<class 'sysml.element.Block'>"
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['primaryHull'].uuid, version=1)

    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['engineeringHull'].uuid, version=1)
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class starship'].parts['primaryHull'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Structure']['Constitution-class starship'].parts['primaryHull'].uuid = "47"
        assert "can't set attribute" in str(info.value)

    assert model['Structure']['Constitution-class starship'].parts['primaryHull'].multiplicity == 1
    assert model['Structure']['Constitution-class starship'].parts['engineeringHull'].multiplicity == 1
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].parts['primaryHull'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].parts['engineeringHull'].multiplicity = -1
        assert "must be a positive int" in str(info.value)

# @pytest.mark.skip('WIP')
def test_block_partProperty_withMultiplicity(model):
    """Add block elements as parts to parent blocks, with multiplicity, using new_part() method"""
    # notes: need to redesign multiplicity constructor and setter
    model['Structure']['Constitution-class starship'].new_part('Nacelle', multiplicity=2)
    model['Structure']['Constitution-class starship'].new_part('Pylon', multiplicity=2)
    assert repr(model['Structure']['Constitution-class starship'].parts['nacelle']) == "\xabblock\xbb \nNacelle"
    assert repr(model['Structure']['Constitution-class starship'].parts['pylon']) == "\xabblock\xbb \nPylon"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['nacelle'])) == "<class 'sysml.element.Block'>"
    assert repr(type(model['Structure']['Constitution-class starship'].parts['pylon'])) == "<class 'sysml.element.Block'>"
    assert model['Structure']['Constitution-class starship'].parts['nacelle'].multiplicity == 2
    assert model['Structure']['Constitution-class starship'].parts['pylon'].multiplicity == 2
    with pytest.raises(TypeError) as info:
        model['Structure']['Constitution-class starship'].parts['pylon'].multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        model['Structure']['Constitution-class starship'].parts['pylon'].multiplicity = -1
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
    # model.new_package('Analysis')
    # model['Analysis'].new_interaction('Warp Field Analysis','testCase')

"""Requirements"""
# @pytest.mark.skip('WIP')
def test_requirements(model):
    """Create a package, labeled 'Requirements', within model which will serve as namespace for the system

    Define two requirement elements, passing in a string name and text field as its constructor arguments
    """
    model.new_package('Requirements') # creates a package, labeled 'Requirements', within model for storing model requirements
    with pytest.raises(TypeError) as info:
        model['Requirements'].new_requirement()
        assert "new_requirement() missing 2 required positional argument: 'name' and 'txt'" in str(info.value)
    model['Requirements'].new_requirement('Top-level', 'A constitution-class starship shall provide a 5-year mission capability to explore strange new worlds, to seek out new life and new civilizations, and to boldly go where no one has gone before.')
    model['Requirements'].new_requirement('Functional', 'A constitution-class starship shall be able to travel at warp 8 or higher')
    assert repr(model['Requirements']['Top-level']) == "\xabrequirement\xbb \nTop-level"
    assert repr(model['Requirements']['Functional']) == "\xabrequirement\xbb \nFunctional"
    assert repr(type(model['Requirements']['Top-level'])) ==  "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['Functional'])) ==  "<class 'sysml.element.Requirement'>"
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
        model['Requirements'].new_dependency()
        assert "new_dependency() missing 3 required positional arguments: 'supplier', 'client', and 'stereotype'" in str(info.value)
    supplier = model['Requirements']['Functional']
    client = model['Requirements']['Top-level']
    model['Requirements'].new_dependency(supplier, client, 'deriveReqt')
    assert repr(model['Requirements']['dependency1'].client) == "\xabrequirement\xbb \nTop-level"
    assert repr(model['Requirements']['dependency1'].supplier) == "\xabrequirement\xbb \nFunctional"
    assert repr(type(model['Requirements']['dependency1'])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements']['dependency1'].supplier)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency1'].client)) == "<class 'sysml.element.Requirement'>"
    assert model['Requirements']['dependency1'].stereotype == "deriveReqt"
    assert uuid.UUID(model['Requirements']['dependency1'].uuid, version=1)
    with pytest.raises(AttributeError) as info:
        model['Requirements']['dependency1'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements']['dependency1'].uuid = "47"
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
    model['Structure']['Constitution-class starship'].new_part('Class-7 Warp Drive')
    reqt1 = model['Requirements']['Functional']
    warpdrive = model['Structure']['Constitution-class starship'].parts['class-7WarpDrive']
    model['Requirements'].new_dependency(reqt1, warpdrive, 'satisfy')
    assert repr(model['Requirements']['dependency2'].supplier) == "\xabrequirement\xbb \nFunctional"
    assert repr(model['Requirements']['dependency2'].client) == "\xabblock\xbb \nClass-7 Warp Drive"
    assert repr(type(model['Requirements']['dependency2'])) == "<class 'sysml.element.Dependency'>"
    assert repr(type(model['Requirements']['dependency2'].supplier)) == "<class 'sysml.element.Requirement'>"
    assert repr(type(model['Requirements']['dependency2'].client)) == "<class 'sysml.element.Block'>"
    assert model['Requirements']['dependency2'].stereotype == "satisfy"
    assert uuid.UUID(model['Requirements']['dependency2'].uuid, version=1)
    with pytest.raises(AttributeError) as info:
        model['Requirements']['dependency2'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['Requirements']['dependency2'].uuid = "47"
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
