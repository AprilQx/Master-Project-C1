# Dual Number Automatic Differentiation

Welcome to the documentation for `dual_autodiff`, a Python package for automatic differentiation using dual numbers.

## Overview

This package implements forward-mode automatic differentiation using dual numbers. It provides a simple and efficient way to compute derivatives of mathematical functions.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from dual_autodiff import Dual

# Create a dual number
x = Dual(2.0, 1.0)  # real part = 2.0, dual part = 1.0

# Basic operations
y = x * x  # Square the number
print(y.real)  # prints 4.0
print(y.dual)  # prints 4.0 (derivative of x^2 is 2x)
```

## Contents

```{toctree}

## Indices and tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`