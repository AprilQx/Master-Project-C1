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


Why Dual Numbers?
----------------

The primary benefit of using dual numbers is that they allow for **forward-mode automatic differentiation**. Here's how it works:

1. **Initialisation**:
   Start with a dual number where the real part represents the function's input value, and the 
   dual part represents the derivative (typically, we initialise the dual part to 1 for differentiation).

2. **Operations**:
   Apply standard mathematical operations (addition, multiplication, etc.) to the dual number.
   The real part will give you the function value, while the dual part will carry the derivative 
   information. Operations are automatically propagated through the function.

3. **Elementary Functions**:
   Functions like ``sin(x)``, ``cos(x)``, ``exp(x)``, and ``log(x)`` are implemented for
   dual numbers in a way that the derivative is computed during the function evaluation.

For example, consider differentiating the function :math:`f(x) = \sin(x)` at a point:

* When we apply the sine function to a dual number, the real part becomes :math:`\sin(a)`, 
  and the dual part becomes :math:`\cos(a) \times b`, where :math:`b` is the derivative 
  (dual part) of the input.

This allows us to compute the function's value and its derivative simultaneously, with minimal 
overhead and high accuracy.

Applications of Dual Numbers
-------------------------

* **Optimisation**:
  Dual numbers are often used in optimisation algorithms, where derivatives are needed to 
  compute gradients and optimise functions.

* **Machine Learning**:
  In neural networks, where backpropagation relies on calculating gradients, dual numbers 
  can efficiently compute the required derivatives.

* **Scientific Computing**:
  Any field that requires solving systems of equations or finding rates of change can 
  benefit from the use of dual numbers for automatic differentiation.

In summary, dual numbers offer a compact and efficient way to compute both function values 
and their derivatives, making them an invaluable tool in various domains, from optimisation 
to machine learning.

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