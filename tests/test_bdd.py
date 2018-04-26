import sysmlpy
import pytest

@pytest.fixture
def model():
    model = sysmlpy.model()
    return model

def test_add_block(model):
    model.add_block('USS Enterprise')
    model.add_block('Primary hull')
    saucersection = model.block['Primary hull']
    assert repr(model.block['USS Enterprise']) == "\xabblock\xbb 'USS Enterprise'"
    assert repr(model.block['Primary hull']) == "\xabblock\xbb 'Primary hull'"

def test_block_parts(model):
    model.add_block(saucersection)
    model.add_relationship(source=model.block['USS Enterprise'], target=[saucersection, model.block['Secondary hull']], stereotype='composition')
    model.block['USS Enterprise'].add_relationship(source=model.block['Primary hull'], target=model.block['Secondary hull'])
    assert repr(model.block['USS Enterprise'].parts) == "[\xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

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
