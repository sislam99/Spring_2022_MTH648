# Temitope Benson's module contains Temitope Benson's functions

import numpy as np

def square_a_number_add_2(x):
	"""
    Temitope Benson's first function.

    Args:
        x (float): Some number.

    Returns:
        float: Returns :math:`y=x^2`
    """

	return x**2 + 2


def pipe_flow(diameter, depth, slope, roughness_n= 0.045):
        
    """
    Temitope Benson's second function.

    Calculates flow in a pipe.

    Args:
        diameter: Pipe diameter in inches or cm.
        depth: Depth of water in inches or cm.
        slope: Slope of the pipe in ft/ft or m/m
        roughness_n: Manning's roughness, default corrugated metal pipe

    Returns:
         Q: Flow in cfs or m^3/sec
    """

   # Assign variables.
     c = 1.49
     D = diameter/12
     d = depth/12
     r = D/2
     n = roughness_n
     S = slope

    # Intermediate calculations.
     theta = 2 * np.arccos((r-d)/r)
     A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
     P = theta * r  # Wetted perimet    
     Rh = A/P  # Hydraulic radius
    # Final calculations.
     v = c/n * Rh**(2/3) * S**0.5
     Q = v * A

     return Q
	