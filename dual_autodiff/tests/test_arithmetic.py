import pytest
from dual_autodiff.dual import Dual

@pytest.fixture

def sample_duals():
    return [
        (Dual(2, 1), Dual(3, 2)),
        (Dual(-2, 1), Dual(3, -2)),
        (Dual(0, 1), Dual(1, 0))
    ]

def test_addition(sample_duals):
    """Test addition of dual numbers"""
    for x, y in sample_duals:
        result = x + y
        assert result.real == pytest.approx(x.real + y.real)
        assert result.dual == pytest.approx(x.dual + y.dual)

def test_addition_with_scalar(sample_duals):
    """Test addition of dual numbers with scalar"""
    scalar = 0.5
    for x, _ in sample_duals:
        result = x + scalar
        assert result.real == pytest.approx(x.real + scalar)
        assert result.dual == pytest.approx(x.dual)

def test_scalar_right_addition(sample_duals):
    """Test right addition with scalar (scalar + dual)"""
    scalar = 2
    for x, _ in sample_duals:
        result = scalar + x
        assert result.real == pytest.approx(scalar + x.real)
        assert result.dual == pytest.approx(x.dual)

def test_multiplication(sample_duals):
    """Test multiplication of dual numbers"""
    for x, y in sample_duals:
        result = x * y
        assert result.real == pytest.approx(x.real * y.real)
        assert result.dual == pytest.approx(x.real * y.dual + x.dual * y.real)

def test_multiplication_with_scalar(sample_duals):
    """Test multiplication of dual numbers with scalar"""
    scalar = 0.5
    for x, _ in sample_duals:
        result = x * scalar
        assert result.real == pytest.approx(x.real * scalar)
        assert result.dual == pytest.approx(x.dual * scalar)

def test_scalar_right_multiplication(sample_duals):
    """Test right multiplication with scalar (scalar * dual)"""
    scalar = 2
    for x, _ in sample_duals:
        result = scalar * x
        assert result.real == pytest.approx(scalar * x.real)
        assert result.dual == pytest.approx(scalar * x.dual)


def test_subtraction(sample_duals):
    """Test subtraction of dual numbers"""
    for x, y in sample_duals:
        result = x - y
        assert result.real == pytest.approx(x.real - y.real)
        assert result.dual == pytest.approx(x.dual - y.dual)

def test_subtraction_with_scalar(sample_duals):
    """Test subtraction of dual numbers with scalar"""
    scalar = 2
    for x, _ in sample_duals:
        result = x - scalar
        assert result.real == pytest.approx(x.real - scalar)
        assert result.dual == pytest.approx(x.dual)
def test_scalar_right_subtraction(sample_duals):
    """Test right subtraction with scalar (scalar - dual)"""
    scalar = 2
    for x, _ in sample_duals:
        result = scalar - x
        assert result.real == pytest.approx(scalar - x.real)
        assert result.dual == pytest.approx(-x.dual)

def test_division(sample_duals):
    """Test division of dual numbers"""
    for x, y in sample_duals:
        if y.real != 0:
            result = x / y
            assert result.real == pytest.approx(x.real / y.real)
            assert pytest.approx(result.dual) == (x.dual * y.real - x.real * y.dual) / (y.real ** 2)

def test_division_with_scalar(sample_duals):
    """Test division of dual numbers with scalar"""
    scalar = 2
    for x, _ in sample_duals:
        result = x / scalar
        assert result.real == pytest.approx(x.real / scalar)
        assert result.dual == pytest.approx(x.dual / scalar)

def test_scalar_right_division(sample_duals):
    """Test right division with scalar (scalar / dual)"""
    scalar = 2
    for x, _ in sample_duals:
        if x.real != 0:
            result = scalar / x
            assert result.real == pytest.approx(scalar / x.real)
            assert result.dual == pytest.approx(-scalar * x.dual / (x.real ** 2))
  

def test_division_zero():
    """Test division by zero cases"""
    x = Dual(2, 1)
    
    with pytest.raises(ZeroDivisionError):
        x / 0
    
    with pytest.raises(ZeroDivisionError):
        x / 0.0
    
    with pytest.raises(ZeroDivisionError):
        x / Dual(0, 0)

def test_scalar_operations_type_error():
    """Test type errors for scalar operations"""
    x = Dual(2, 1)
    invalid_scalar = "2"
    
    with pytest.raises(TypeError):
        invalid_scalar + x
    with pytest.raises(TypeError):
        invalid_scalar * x
    with pytest.raises(TypeError):
        invalid_scalar / x
    with pytest.raises(TypeError):
        invalid_scalar - x