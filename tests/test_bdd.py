import sysml
import pytest

@pytest.fixture
def model():
    "Create a SysML model instance"
    model = sysml.Model('USS Enterprise')
    return model

@pytest.fixture
def create_package1():
    "Create a package in newly created model"
    model.add_package('NCC-1701')
    return model

@pytest.fixture
def create_blocks(model):
    "Add blocks in newly created model"
    model.add_block('Primary hull')
    model.add_block('Secondary hull')
    saucersection = model.add_block['Primary hull']
    return model

def test_add_blocks(add_blocks):
    assert repr(model.block['NCC-1701']) == "\xabblock\xbb 'NCC-1701'"
    assert repr(model.block['Primary hull']) == "\xabblock\xbb 'Primary hull'"
    assert repr(saucersection) == "\xabblock\xbb 'Primary hull'"

@pytest.fixture
def add_block_relationships(add_blocks):
    "Define relationships between blocks in model"
    model.add_relationship(source = model.block['NCC-1701'], target = [saucersection, model.block['Secondary hull']], stereotype='composition')
    return model

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
