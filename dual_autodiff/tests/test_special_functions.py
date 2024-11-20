import pytest
import math
from dual_autodiff.dual import Dual

@pytest.fixture

def special_values():
    return [
        Dual(1, 1),
        Dual(2, 1),
        Dual(0.5, 1),
        Dual(math.e, 1)
    ]

def test_exp(special_values):
    """Test exponential function"""
    for x in special_values:
        result = x.exp()
        assert result.real == pytest.approx(math.exp(x.real))
        assert result.dual ==pytest.approx( x.dual * math.exp(x.real))