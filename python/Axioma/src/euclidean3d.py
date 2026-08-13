"""
Euclidean3D

Purpose
-------
To calculate fundamental geometric and physical measurements of 3D shapes.

The supported 3D shapes include:
    - Sphere


Calculations
------------
The properties and metrics calculated within these shapes include:
    - Surface Area  (all shapes)
    - Volume        (all shapes)

Author
------
Allan Smart
Blackbit Analytics © 2026

"""

#---------------------------------------
#           Import Libraries
#---------------------------------------
from abc import ABC, abstractmethod
import math

#---------------------------------------
#           Shape - Parent Class 3D
#---------------------------------------
class Shape3D(ABC):

    """ 
    An abstract base class representing a generic three-dimensional shape.

    This class serves as a blueprint for all 3D geometric shapes. It enforces
    that any subclass must implement properties to calculate its basic geometric
    measurements. Attempting to instantiate a subclass without defining these 
    required abstract properties will raise a `TypeError`.

    Parameters
    ----------
    name : str
        The identifying name of the specific 3D shape (e.g., Sphere).

    Attributes
    ----------
    name : str
        The identifying name of the specific 3D shape.

    See Also
    --------
    abc.ABC : The Python standard library helper class for defining abstract
        base classes.

    Notes
    -----
    Subclasses must override and implement both 'surface area' and 'volume'
    properties. If either property is omitted in a child class. Python prevents
    object creation at runtime with `TypeError`.
    """

    # Constructor method to initialise instance attributes
    def __init__(self, name: str):
        self.name = name
    
    # Ensuring that surface area must be included all child classes
    @property
    @abstractmethod
    def surface_area(self) -> float:
        pass

    # Ensuring that volume must be included in all child classes
    @property
    @abstractmethod
    def volume(self) -> float:
        pass

#---------------------------------------
#           Sphere - Child Class
#---------------------------------------
class Sphere(Shape3D):

    pass