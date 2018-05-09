import sysml
import pytest
import uuid

# Notes: block elements with starting property attributes should be broken down into granular blocks and assigned id's & relationships upon assimilation into model.
@pytest.fixture
def model():
    "Create a SysML model instance"
    model = sysml.Model('USS Enterprise')
    return model

@pytest.fixture
def set_key_assigned_model_elements(model):
    "Set model elements using valid key"
    enterprise = sysml.Block('NCC-1701')
    saucersection = sysml.Block('Primary hull')
    model["block-1"] = enterprise
    model["block-2"] = saucersection
    model["block-3"] = sysml.Block('Secondary hull')
    return model

def test_key_assigned_model_elements(set_key_assigned_model_elements):
    "Set and get model elements or relationships using valid key"
    model = set_key_assigned_model_elements
    assert repr(model["block-1"]) == "\xabblock\xbb 'NCC-1701'"
    assert repr(model["block-2"]) == "\xabblock\xbb 'Primary hull'"
    assert repr(model["block-3"]) == "\xabblock\xbb 'Secondary hull'"
    with pytest.raises(TypeError):
        model["block-1"] = "Darmok"
    with pytest.raises(ValueError):
        model["blob-1"] = sysml.Block('Jalad')

def test_element_has_valid_uuid(set_key_assigned_model_elements):
    "Model elements should be assigned a uuid upon assimilation into model"
    model = set_key_assigned_model_elements
    assert uuid.UUID(model["block-1"].uuid, version=1)

def test_attribute_assigned_model_elements(set_key_assigned_model_elements):
    "Set and get model elements using valid key"
    warpcore = sysml.Block('warp core')
    model.elements = {"block-1":warpcore}
    # model.elements = {'block-1': 42}
    assert repr(model.elements['block-1']) == "\xabblock\xbb 'warp core'"
    with pytest.raises(KeyError):
        repr(model.elements['block-2'])
    # with pytest.raises(TypeError):
    #     model.elements = {'block-1': 42}
    # with pytest.raises(ValueError):
    #     model.elements = {'blob-1': sysml.Block('Jalad')}

def test_generateKey_elements(set_key_assigned_model_elements):
    model = set_key_assigned_model_elements
    assert model._generateKey(model["block-1"], 9999) == 'block-4'
    with pytest.raises(TypeError):
        model._generateKey("block-1", 9999)

@pytest.fixture
def set_key_assigned_model_relationships(set_key_assigned_model_elements):
    "Set model relationships using valid key"
    model = set_key_assigned_model_elements
    model["partProperty-1"] = {"source":"block-1", "target":["block-2", "block-3"]}
    return model

def test_key_assigned_model_relationships(set_key_assigned_model_elements):
    "Get model relationships using valid key"
    model = set_key_assigned_model_elements
    partProperty1 = model["partProperty-1"]
    assert partProperty1["source"] == "block-1"
    assert partProperty1["target"][0] == "block-2"
    assert partProperty1["target"][1] == "block-3"
    # with pytest.raises(TypeError):
    #     model.relationships = {"partProperty-1": str('Darmok')}
    # with pytest.raises(ValueError):
    #     model.relationships = {"blob-1": sysml.Block('Jalad')}

@pytest.fixture
def set_attribute_assigned_relationships(set_key_assigned_model_elements):
    "Define relationships between model elements as a dictionary of source-target pairs"
    model = set_key_assigned_model_elements
    model.relationships = {"partProperty-1": {"source":"block-1", "target":["block-2", "block-3"]}}
    return model

def test_attribute_assigned_relationships(set_attribute_assigned_relationships):
    "Model relationships should return id Keys of model elements as a dictionary of source-target pairs, but should internally use uuid's"
    model = set_relationships
    partProperty1 = model["partProperty-1"]
    assert partProperty1["source"] == "block-1"
    assert partProperty1["target"][0] == "block-2"
    assert partProperty1["target"][1] == "block-3"
    with pytest.raises(TypeError):
        model.relationships = {"partProperty-1": str('Darmok')}
    with pytest.raises(ValueError):
        model.relationships = {"blob-1": sysml.Block('Jalad')}

# @pytest.fixture
# def add_blocks(model):
#     "add block(s) to model using built-in 'add_block()' method"
#     enterprise = sysml.Block('NCC-1701')
#     saucersection = sysml.Block('Primary hull')
#     model.add_block(enterprise)
#     model.add_block(saucersection, sysml.Block('Secondary hull'))
#     return model
#
# def test_add_blocks(add_blocks):
#     assert repr(model.elements) == "[\xabblock\xbb 'NCC-1701', \xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

"""
def test_block_parts(add_block_relationships):
    assert repr(model.block['NCC-1701'].parts) == "[\xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

def test_block_values(model):
    valueProperty = {'class':'Constitution','P/N':'NCC-1701'}
    model.block['USS Enterprise'].add_values(valueProperty)
    assert model.block['USS Enterprise'].values == {'P/N': 'NCC-1701', 'class': 'Constitution'}

def test_block_references():
    model = sysml.BlockDefinitionDiagram('warp drive model')
    model.new_block('antimatter')
    model.new_block('antimatter injector')
    model.new_block('dilithium crystal chamber')
    model.new_block(label='warp core', parts=[model.block['antimatter injector'], model.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=model.block['antimatter']
                    )
    model.block['warp core'].add_references(model.block['antimatter'])
    assert repr(model.block['warp core'].references) == "[\xabblock\xbb 'antimatter']"

def test_block_flowProperties():
    model = sysml.BlockDefinitionDiagram('warp drive model')
    model.new_block('antimatter')
    model.new_block('antimatter injector')
    model.new_block('dilithium crystal chamber')
    model.new_block(label='warp core', parts=[model.block['antimatter injector'], model.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=model.block['antimatter']
                    )
    model.block['warp core'].add_flowProperties({'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}})
    assert model.block['warp core'].flowProperties == {'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}}
"""
