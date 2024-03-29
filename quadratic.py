# -*- coding: utf-8 -*-
"""quadratic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vCI0-yJ2zuZA5_XBABb3QiUvoKN-7SPd
"""

from math import sqrt

class Quadratic_equation:
  def __init__(self, a,b,c):
    self.a = a
    self.b = b
    self.c = c
    self.d = self.b**2 - 4*self.a*self.c

  def roots(self):
    x1 = (-self.b + sqrt(self.d))/2*self.a
    x2 = (-self.b - sqrt(self.d))/2*self.a
    x = -self.b/2*self.a
    
    if self.d > 0:
      return x1, x2
      
    elif self.d == 0:
      return x
eq1 = Quadratic_equation(1, -4, 3)

print(Quadratic_equation.roots(eq1))