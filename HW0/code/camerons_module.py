# Cameron's module contains Cameron's functions

import numpy as np

def random_integer(x):
	"""
    Cameron's first function.

    Args:
        x (float): Some positive integer.

    Returns:
        int: Returns a random integer between 1 and x (inclusive)
    """

	return np.random.randint(x)+1

def successor_function(x):
	"""
    Cameron's second function.

    Args:
        x (float): Some number.

    Returns:
        float: Returns :math:`y=x+1`
    """

	return x+1

	
