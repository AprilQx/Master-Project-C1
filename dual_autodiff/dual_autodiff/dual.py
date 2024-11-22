import numpy as np
import math 
from typing import Union

class Dual:
    """
    A class to represent a dual number.
    """
    def __init__(self, real: Union[int, float], dual: Union[int, float]=0.0):
        """
        Initialize a dual number with validation for special values

        Args:
            real (Union[int, float]): The real part of the dual number
            dual (Union[int, float], optional): The dual part of the dual number. Defaults to 0.0.
        
        Raises:
            ValueError: Infinity is not allowed in dual numbers
            ValueError: NaN is not allowed in dual numbers
        """
        if math.isinf(real) or math.isinf(dual):
            raise ValueError("Infinity is not allowed in dual numbers")
        if math.isnan(real) or math.isnan(dual):
            raise ValueError("NaN is not allowed in dual numbers")
        self.real = float(real)
        self.dual = float(dual)

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
        return Dual(self.real / other.real, (self.dual * other.real - self.real * other.dual) / (other.real ** 2))
    
    def sin(self):
        """
        the dual part of the sin is calculated using the formula:"""
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))
    
    def cos(self):
        """
        the dual part of the cos is calculated using the formula:"""
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))
    
    def exp(self):
        """
        the dual part of the exp is calculated using the formula:"""
        return Dual(math.exp(self.real), self.dual * math.exp(self.real))
    
    def log(self):
        """
        the dual part of the log is calculated using the formula:"""
        return Dual(math.log(self.real), self.dual / self.real)
    

    def sqrt(self):
        """
        the dual part of the sqrt is calculated using the formula:"""
        return Dual(math.sqrt(self.real), self.dual / (2 * math.sqrt(self.real)))
    

    def power(self, n):
        """
        the dual part of the power is calculated using the formula:"""
        return Dual(self.real ** n, n * (self.real ** (n-1)) * self.dual)
    

    def tan(self):
        """
        the dual part of the tan is calculated using the formula:"""
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))
    
   