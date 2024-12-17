# dual_autodiff

Dual number automatic differentiation package for Python.

## Overview

`dual_autodiff` is a Python package that provides automatic differentiation using dual numbers. This package allows you to compute derivatives alongside function evaluations, making it useful for optimization, machine learning, and other applications requiring derivative calculations.

## Features

- Dual number arithmetic operations (addition, subtraction, multiplication, division)
- Trigonometric functions (sin, cos, tan)
- Exponential and logarithmic functions
- Square root and power functions
- Automatic differentiation using dual numbers

## Installation

To install the package, run:

```bash
pip install -e .
```

## Example Usage

```python
from dual_autodiff import Dual

# Define a dual number
x = Dual(2.0, 1.0)

# Perform operations
y = x * x 
print(f"Value: {y.real}")     # 4.0
print(f"Derivative: {y.dual}") # 4.0
```

## Documentation
Full documentation is available in the docs directory. You can build the documentation using Sphinx:
```bash
cd docs
make html
```
The generated documentation will be available in docs/_build/html (currently the html is built already)
```bash
open index.html
```
This will open your documentation in your default web browser. No need for Live Server or online hosting if you just want to check how your documentation looks!

## Examples
Example Jupyter notebooks demonstrating the usage of the package are available in the examples directory:

`dual_autodiff.ipynb`
`dual_autodiff_tutorial.ipynb`

## Running Tests
To run the tests, use `pytest`:
```bash
pytest -s tests /*
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on Gitlab or Github.

## Contact
For any questions or inquiries, please contact the author Xueqing Xu