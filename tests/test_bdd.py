import sysmlpy as sysml
import pytest

def test_new_block():
    bdd = sysml.BlockDefinitionDiagram('USS Enterprise BDD')
    bdd.new_block('USS Enterprise')
    assert repr(bdd.block['USS Enterprise']) == "\xabblock\xbb 'USS Enterprise'"

def test_add_block():
    bdd = sysml.BlockDefinitionDiagram('Enterprise BDD')
    saucersection = sysml.Block('Primary hull')
    bdd.add_blocks(saucersection)
    assert repr(bdd.block['Primary hull']) == "\xabblock\xbb 'Primary hull'"

def test_block_parts():
    bdd = sysml.BlockDefinitionDiagram('Enterprise BDD')
    bdd.new_block('USS Enterprise')
    saucersection = sysml.Block('Primary hull')
    bdd.add_blocks(saucersection)
    bdd.new_block('Secondary hull')
    bdd.block['USS Enterprise'].add_parts(bdd.block['Primary hull'],bdd.block['Secondary hull'])
    assert repr(bdd.block['USS Enterprise'].parts) == "[\xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

def test_block_values():
    bdd = sysml.BlockDefinitionDiagram('Enterprise BDD')
    bdd.new_block('USS Enterprise')
    valueProperty = {'class':'Constitution','P/N':'NCC-1701'}
    bdd.block['USS Enterprise'].add_values(valueProperty)
    assert bdd.block['USS Enterprise'].values == {'P/N': 'NCC-1701', 'class': 'Constitution'}

def test_block_references():
    bdd = sysml.BlockDefinitionDiagram('warp drive BDD')
    bdd.new_block('antimatter')
    bdd.new_block('antimatter injector')
    bdd.new_block('dilithium crystal chamber')
    bdd.new_block(label='warp core', parts=[bdd.block['antimatter injector'], bdd.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=bdd.block['antimatter']
                    )
    bdd.block['warp core'].add_references(bdd.block['antimatter'])
    assert repr(bdd.block['warp core'].references) == "[\xabblock\xbb 'antimatter']"

def test_block_flowProperties():
    bdd = sysml.BlockDefinitionDiagram('warp drive BDD')
    bdd.new_block('antimatter')
    bdd.new_block('antimatter injector')
    bdd.new_block('dilithium crystal chamber')
    bdd.new_block(label='warp core', parts=[bdd.block['antimatter injector'], bdd.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=bdd.block['antimatter']
                    )
    bdd.block['warp core'].add_flowProperties({'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}})
    assert bdd.block['warp core'].flowProperties == {'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}}


