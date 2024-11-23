Theory
======

What are Dual Numbers?
---------------------

A dual number is an extension of real numbers, similar to complex numbers. While complex numbers use an imaginary unit :math:`i` where :math:`i^2 = -1`, dual numbers use a dual unit :math:`\epsilon` where :math:`\epsilon^2 = 0`.

Structure
~~~~~~~~~
A dual number has the form:

.. math::

   x = a + b\epsilon

where:
* :math:`a` is the real part
* :math:`b` is the dual part
* :math:`\epsilon` is the dual unit with :math:`\epsilon^2 = 0`

Basic Operations
--------------

Addition
~~~~~~~~
The addition of two dual numbers follows:

.. math::

   (a + b\epsilon) + (c + d\epsilon) = (a + c) + (b + d)\epsilon

Multiplication
~~~~~~~~~~~~~
The multiplication uses the property :math:`\epsilon^2 = 0`:

.. math::

   (a + b\epsilon)(c + d\epsilon) = ac + (bc + ad)\epsilon + bd\epsilon^2 = ac + (bc + ad)\epsilon

Division
~~~~~~~~
Division is defined for dual numbers with non-zero real part:

.. math::

   \frac{a + b\epsilon}{c + d\epsilon} = \frac{a}{c} + \frac{bc - ad}{c^2}\epsilon

Automatic Differentiation
-----------------------

Forward Mode
~~~~~~~~~~~
Forward-mode automatic differentiation computes derivatives alongside function evaluation.
When we create a dual number :math:`x = a + \epsilon`, the dual part tracks the derivative:

.. code-block:: python

   x = Dual(2.0, 1.0)  # 2 + ε
   y = x * x           # 4 + 4ε
   print(y.dual)       # 4.0 (derivative of x² at x=2)

Common Functions
~~~~~~~~~~~~~~
Basic derivatives are implemented as:

.. math::

   \sin(a + b\epsilon) &= \sin(a) + b\cos(a)\epsilon
   
   \cos(a + b\epsilon) &= \cos(a) - b\sin(a)\epsilon
   
   \exp(a + b\epsilon) &= \exp(a) + b\exp(a)\epsilon
   
   \log(a + b\epsilon) &= \log(a) + \frac{b}{a}\epsilon

Example Usage
-----------

Computing Simple Derivatives
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Compute derivative of sin(x²)
   def f(x):
       return (x * x).sin()
   
   x = Dual(2.0, 1.0)
   result = f(x)
   print(f"f'(2) = {result.dual}")

Chain Rule Application
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Compute derivative of exp(sin(x))
   def g(x):
       return x.sin().exp()
   
   x = Dual(1.0, 1.0)
   result = g(x)
   print(f"g'(1) = {result.dual}")