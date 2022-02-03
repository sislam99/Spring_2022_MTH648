# Makenzie's module contains Makenzie's functions

import numpy as np

def log_of(x):
	"""
    Makenzie's first function.

    Args:
        x (float): Some number.

    Returns:
        float: Returns :math:`y=ln(x)`
    """

	return np.log(x)

def factorial(x):
	"""
    Makenzie's second function.

    Args:
        x (int): Some number.

    Returns:
        int: Returns :math:`y=x!`
    """
  temp=1
  for i in range(1,x+1):
    temp*=i
	return temp

	
