import pytest
import sys
from dual_autodiff.dual import Dual
import math

def test_large_values():
    """Test large values"""
    large_val = sys.float_info.max / 2
    x = Dual(large_val, 1)
    y = Dual(2, 1)

    result = x * y
    assert not math.isinf(result.real)
    assert not math.isinf(result.dual)

def test_small_values():
    """Test handling of small values"""
    small_val = sys.float_info.min * 2
    x = Dual(small_val, small_val)
    y = Dual(small_val, small_val)
    
    result = x * y
    assert result.real >= 0
    assert result.dual >= 0

def test_special_values():
    """Test handling of special float values"""
    with pytest.raises(ValueError):
        x = Dual(float('inf'), 1)
    
    with pytest.raises(ValueError):
        x = Dual(float('nan'), 1)