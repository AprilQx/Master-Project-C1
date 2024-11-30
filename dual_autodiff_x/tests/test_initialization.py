import pytest
from dual_autodiff.dual import Dual

def test_basic_initialization():
    """Test various initialization types"""
    x= Dual(1,2)
    assert x.real == 1.0 
    assert x.dual == 2.0

    x= Dual(1.0,2.0)
    assert x.real == 1.0
    assert x.dual == 2.0

    x= Dual(1,2.0)
    assert x.real == 1.0
    assert x.dual == 2.0

def test_zero_initialization():
    """Test zero initialization"""
    x= Dual.zero()
    assert x.real == 0.0
    assert x.dual == 0.0

def test_negative_initialization():
    """Test negative initialization"""
    x= Dual(-1,-2)
    assert x.real == -1.0
    assert x.dual == -2.0

    x= Dual(-1.0,-2.0)
    assert x.real == -1.0
    assert x.dual == -2.0

    x= Dual(-1,-2.0)
    assert x.real == -1.0
    assert x.dual == -2.0

    