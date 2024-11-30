import numpy as np
cimport numpy as np

from libc.math cimport sin as csin, cos as ccos, exp as cexp
from libc.math cimport log as clog, sqrt as csqrt, tan as ctan
from libc.math cimport pow as cpow, isnan, isinf


cdef class Dual:
    """
    A class to represent a dual number.
    """
    cdef public double real
    cdef public double dual
    
    def __init__(self, double real, double dual=0.0):
        """
        Initialize a dual number with validation for special values

        Args:
            real (Union[int, float]): The real part of the dual number
            dual (Union[int, float], optional): The dual part of the dual number. Defaults to 0.0.
        
        Raises:
            ValueError: Infinity is not allowed in dual numbers
            ValueError: NaN is not allowed in dual numbers
        """

        if isinf(real) or isinf(dual):
            raise ValueError("Infinity is not allowed in dual numbers")
        if isnan(real) or isnan(dual):
            raise ValueError("NaN is not allowed in dual numbers")
        self.real = real
        self.dual = dual
    
    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})"

    def __str__(self):
        return self.__repr__()
    @staticmethod
    def zero():
        #no access to instance variables
        """Create a zero dual number"""
        return Dual(0.0, 0.0)
    
    def __add__(self, other):
        """
        The sum of two dual numbers is calculated using the formula:"""
        if isinstance(other, (int, float)):
            return Dual(self.real + other, self.dual) #Handle regular numbers
        return Dual(self.real + other.real, self.dual + other.dual) #Handle dual numbers
    
    def __radd__(self, other):
        """
        Right addition with scalar: scalar + dual
        """
        if isinstance(other, (int, float)):
            return Dual(other + self.real, self.dual)
        raise TypeError(f"unsupported operand type for +: '{type(other)}' and 'Dual'")

    def __mul__(self, other):
            """
            The product of two dual numbers is calculated using the formula:"""
            if isinstance(other, (int, float)):
                return Dual(self.real * other, self.dual * other) #Handle regular numbers
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)#Handle dual numbers
    
    def __rmul__(self, other):
        """
        Right multiplication with scalar: scalar * dual
        """
        if isinstance(other, (int, float)):
            return Dual(other * self.real, other * self.dual)
        raise TypeError(f"unsupported operand type for *: '{type(other)}' and 'Dual'")
   
    def __sub__(self, other):
        """
        The difference of two dual numbers is calculated using the formula:"""
        if isinstance(other, (int, float)):
            return Dual(self.real - other, self.dual)
        return Dual(self.real - other.real, self.dual - other.dual)
    def __rsub__(self, other):
        """
        Right subtraction with scalar: scalar - dual
        """
        if isinstance(other, (int, float)):
            return Dual(other - self.real, -self.dual)
        raise TypeError(f"unsupported operand type for -: '{type(other)}' and 'Dual'")
        
    def __rtruediv__(self, other):
        """
        Right division with scalar: scalar / dual
        Calculated as: a/(b + cε) = (a/b) + (-ac/b^2)ε
        """
        if isinstance(other, (int, float)):
            return Dual(other / self.real, -other * self.dual / (self.real ** 2))
        raise TypeError(f"unsupported operand type for /: '{type(other)}' and 'Dual'")
       
    
    def __truediv__(self, other):
        """
        the dual part of the division is calculated using the formula:
        (a + bε) / (c + dε) = (a/c) + ((b*c - a*d) / c^2)ε
        """
        if isinstance(other, (int, float)):
            return Dual(self.real / other, self.dual / other)
        return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real * other.real))
    
    cpdef Dual sin(self):
        """
        the dual part of the sin is calculated using the formula:"""
        return Dual(csin(self.real), self.dual * ccos(self.real))
    
    cpdef Dual cos(self):
        """
        the dual part of the cos is calculated using the formula:"""
        return Dual(ccos(self.real), -self.dual * csin(self.real))
    
    cpdef Dual exp(self):
        """
        the dual part of the exp is calculated using the formula:"""
        cdef double exp_real = cexp(self.real)
        return Dual(exp_real, self.dual * exp_real)
    
    cpdef Dual log(self):
        """
        the dual part of the log is calculated using the formula:"""
        return Dual(clog(self.real), self.dual / self.real)

    cpdef Dual sqrt(self):
        """
        the dual part of the sqrt is calculated using the formula:"""
        cdef double sqrt_real = csqrt(self.real)
        return Dual(sqrt_real, self.dual / (2.0 * sqrt_real))
    

    cpdef Dual power(self, double n):
        """Compute power of dual number."""
        return Dual(
            cpow(self.real, n),
            n * cpow(self.real, n-1.0) * self.dual
        )
    
    cpdef Dual tan(self):
        """Compute tangent of dual number."""
        cdef double cos_real = ccos(self.real)
        return Dual(ctan(self.real), self.dual / (cos_real * cos_real))
    
    
   