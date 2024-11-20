import pytest
import math
from dual_autodiff.dual import Dual

@pytest.fixture
def trg_values():
    return [
        Dual(0, 1),
        Dual(math.pi/6, 1),
        Dual(math.pi/4, 1),
        Dual(math.pi/3, 1),
        Dual(math.pi/2, 1)
    ]

def test_sin(trg_values):
    """Test sin function"""
    for x in trg_values:
        result = x.sin()
        assert result.real == math.sin(x.real)
        assert result.dual == x.dual * math.cos(x.real)

def test_cos(trig_values):
    """Test cosine function"""
    for x in trig_values:
        result = x.cos()
        assert result.real == pytest.approx(math.cos(x.real))
        assert result.dual == pytest.approx(-x.dual * math.sin(x.real))

def test_tan(trig_values):
    """Test tangent function"""
    for x in trig_values:
        if math.cos(x.real) != 0:
            result = x.tan()
            assert result.real == pytest.approx(math.tan(x.real))
            assert result.dual == pytest.approx(x.dual / (math.cos(x.real) ** 2))