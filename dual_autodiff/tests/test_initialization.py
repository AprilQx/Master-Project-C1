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
def test_repr():
    """Test the __repr__ function"""
    x = Dual(1.0, 2.0)
    assert repr(x) == "Dual(real=1.0, dual=2.0)"
    
    # Test with negative numbers
    x = Dual(-1.0, -2.0)
    assert repr(x) == "Dual(real=-1.0, dual=-2.0)"
    
    # Test with zero
    x = Dual(0.0, 0.0)
    assert repr(x) == "Dual(real=0.0, dual=0.0)"

def test_str():
    """Test the __str__ function"""
    x = Dual(1.0, 2.0)
    assert str(x) == "Dual(real=1.0, dual=2.0)"
    
    # Test that str and repr give the same result
    assert str(x) == repr(x)
    
    # Test with different values
    x = Dual(-1.0, -2.0)
    assert str(x) == "Dual(real=-1.0, dual=-2.0)"
    assert str(x) == repr(x)
    
    x = Dual(0.0, 0.0)
    assert str(x) == "Dual(real=0.0, dual=0.0)"
    assert str(x) == repr(x)
    