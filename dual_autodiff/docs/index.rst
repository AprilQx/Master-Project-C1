Dual Number Automatic Differentiation
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   theory
   dual_autodiff.ipynb

Quick Example
------------

.. code-block:: python

    from dual_autodiff import Dual
    x = Dual(2.0, 1.0)
    y = x * x 
    print(f"Value: {y.real}")     # 4.0
    print(f"Derivative: {y.dual}") # 4.0

