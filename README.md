# dual_autodiff

[![Documentation Status](https://readthedocs.org/projects/dual-autodiff/badge/?version=latest)](https://dual-autodiff.readthedocs.io/en/latest/?badge=latest)

Dual number automatic differentiation package for Python.

## Documentation

Full documentation is available at: https://dual-autodiff.readthedocs.io/

## Quick Start
```python
from dual_autodiff import Dual

x = Dual(2.0, 1.0)
y = x * x 
print(f"Value: {y.real}")     # 4.0
print(f"Derivative: {y.dual}") # 4.0
```

## Installation

```bash
pip install -e .
```