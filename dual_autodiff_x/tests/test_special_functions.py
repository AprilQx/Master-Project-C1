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

def test_log(special_values):
    """Test logarithmic function"""
    for x in special_values:
        if x.real > 0:
            result = x.log()
            assert result.real == pytest.approx(math.log(x.real))
            assert result.dual == pytest.approx(x.dual / x.real)

def test_power(special_values):
    """Test power function"""
    for x in special_values:
        n = 2
        result = x.power(n)
        assert result.real == pytest.approx(x.real ** n)
        assert result.dual == pytest.approx(n * (x.real ** (n-1)) * x.dual)

def test_sqrt(special_values):
    """Test square root function"""
    for x in special_values:
        if x.real > 0:
            result = x.sqrt()
            assert result.real == pytest.approx(math.sqrt(x.real))
            assert result.dual == pytest.approx(x.dual / (2 * math.sqrt(x.real)))