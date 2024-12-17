# dual_autodiff

Dual number automatic differentiation package for Python.

## Overview

`dual_autodiff_x` is a Python package that provides automatic differentiation using dual numbers. This package allows you to compute derivatives alongside function evaluations, making it useful for optimization, machine learning, and other applications requiring derivative calculations.

## Features

- Dual number arithmetic operations (addition, subtraction, multiplication, division)
- Trigonometric functions (sin, cos, tan)
- Exponential and logarithmic functions
- Square root and power functions
- Automatic differentiation using dual numbers

## Installation

### Direct pip install

To install the package directly using pip on a linux systme, run:

```bash
pip install dual_autodiff_x-0.1.0-cp310-cp310-linux_x86_64.whl
```

### Using Docker
To build and run the Docker container, follow these steps:
1. Build the Docker image:
```bash
docker build --no-cache -t dual_autodiff_test .
```
2. Run the Docker container:
```bash
docker run -p 8888:8888 dual_autodiff_test
```  