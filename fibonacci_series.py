# -*- coding: utf-8 -*-
"""fibonacci_series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_gy2ayEbQTTxwrjPawRH51xTfEGbeIDb
"""

# Function for nth Fibonacci number 
  
def Fibonacci(n):
  if n<0:
    print("Incorrect input")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))

