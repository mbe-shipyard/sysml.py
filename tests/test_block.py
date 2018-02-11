import sysmlpy as sysml
import pytest

def test_new_block():
    saucersection = sysml.Block('Primary hull')
    assert repr(saucersection) == "\xabblock\xbb 'Primary hull'"

def test_block_properties():
    antimatter = sysml.Block('antimatter')
    antimatterinjector = sysml.Block('antimatter injector')
    dilithiumcrystalchamber = sysml.Block('dilithium crystal chamber')
    warpcore = sysml.Block(label='warp core', parts=[antimatterinjector, dilithiumcrystalchamber],
                     flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                     references=[antimatter])
    assert repr(warpcore) == "\xabblock\xbb 'warp core'"

