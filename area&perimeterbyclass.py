# -*- coding: utf-8 -*-
"""Area&PerimeterByClass.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ajOo-1GoOVqy_WluyoN5G7S_RagkqA8C
"""

class Circle():
  def _init_(self, r):
    self.radius = r
  
  def area(self):
    return self.radius**2*3.14

  def perimeter(self):
    return 2*self.radius*3.14

NewCircle = Circle(8)
print("Area of Circle is", NewCircle.area())
print("Perimeter of Circle is", NewCircle.perimeter())

