# dual_autodiff


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