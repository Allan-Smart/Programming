"""
Euclidean2D

Purpose
-------
To calculate fundamental geometric and physical measurements of 2D shapes.

The supported 2D shapes include:
    - Circle
    - Square
    - Rectangle
    - Triangles
        - Equilateral Triangle
        - Right Angle Triangle
        - Isosceles Triangle
        - Scalene Triangle
    - Parallelogram (To be done)
    - Trapezoid     (To be done)
    - Regular Pentagon
    - Regular Hexagon 
    - Regular Octagon

Calculations
------------
The properties and metrics calculated within these shapes include:
    - Area              (all shapes)
    - Perimeter         (all shapes)
    - Arc Length        (specific to Circle)
    - Sector Area       (specific to Circle)
    - Segment Area      (specific to Circle)
    - Chord Length      (specific to Circle)
    - Sagitta           (specific to Circle)
    - Diagonal
    - Centroid
    - Circumradius
    - Second Moment of Area
    - and others...

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
#           Shape - Parent Class 2D
#---------------------------------------
class Shape2D(ABC):
    
    """
    An abstract base class representing a generic two-dimensional shape.

    This class serves as a blueprint for all 2D geometric shapes. It enforces 
    that any subclass must implement properties to calculate its basic 
    geometric measurements. Attempting to instantiate a subclass without 
    defining these required abstract properties will raise a `TypeError`.

    Parameters
    ----------
    name : str
        The identifying name of the specific 2D shape (e.g., 'Circle').

    Attributes
    ----------
    name : str
        The identifying name of the specific 2D shape.

    See Also
    --------
    abc.ABC : The Python standard library helper class for defining abstract 
        base classes.

    Notes
    -----
    Subclasses must override and implement both the `area` and `perimeter` 
    properties. If either property is omitted in a child class, Python 
    prevents object creation at runtime with a `TypeError`.
    """

    # Constructor method to initialise instance attributes
    def __init__(self, name: str):
        self.name = name

    # Ensuring that area must be included in all child classes
    @property
    @abstractmethod
    def area(self) -> float:
        pass
    
    # Ensuring that perimeter must be included in all child classes    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

#---------------------------------------
#           Circle - Child Class
#---------------------------------------
class Circle(Shape2D):
    
    """
    A concrete implementation of a 2D shape representing a circle.

    Provides geometric calculations for standard circle metrics (area, 
    perimeter) as well as advanced circle components like arcs, sectors, 
    segments, chords, and sagittas. It enforces strict type and value 
    validation on the radius.

    Parameters
    ----------
    radius : float or int
        The radius of the circle. Must be greater than zero.

    Attributes
    ----------
    radius : float
        The validated radius of the circle.
    name : str
        The identifying name of the shape, hardcoded to 'Circle'.

    Raises
    ------
    TypeError
        If the provided radius is not an integer or a float.
    ValueError
        If the provided radius is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    # Constructor method to initialise instance attributes
    def __init__(self, radius: float):
        super().__init__('Circle')
        self.radius = radius  # Triggers the setter

    @property
    def radius(self) -> float:
        """
        float: The radius of the circle. Enforces positive numeric constraints.
        """
        return self._radius
    
    # Radius error checking
    @radius.setter
    def radius(self, radius: float) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be an integer or float')
        if radius <= 0:
            raise ValueError('Radius length must be greater than 0')
        self._radius = radius
    
    # To calculate the area of a circle
    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the circle.
        """
        return math.pi * self._radius ** 2
    
    # To calculate the perimeter(circumference) of a circle
    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self._radius
    
    # Circle functions
    def _validate_degrees(self, angle_degrees: float) -> None:
        """
        Validate that an input angle is a numeric value between 0 and 360 degrees.

        Parameters
        ----------
        angle_degrees : float or int
            The angle to validate, measured in degrees.

        Raises
        ------
        TypeError
            If the angle is not an integer or a float.
        ValueError
            If the angle falls outside the closed interval.
        """
        if not isinstance(angle_degrees, (int, float)):
            raise TypeError('Angle must be an integer or float')
        if angle_degrees < 0 or angle_degrees > 360:
            raise ValueError('Angle must be between 0 and 360 degrees')

    # To calculate the arc length of a circle
    def arc_length(self, angle_degrees: float) -> float:
        """
        Calculate the length of an arc for a given central angle.

        Parameters
        ----------
        angle_degrees : float or int
            The central angle subtending the arc, in degrees.

        Returns
        -------
        float
            The outer distance along the arc length.
        """
        self._validate_degrees(angle_degrees)
        return math.radians(angle_degrees) * self.radius
    
    # To calculate the sector area of a circle
    def sector_area(self, angle_degrees: float) -> float:
        """
        Calculate the area of a circular sector bounded by a central angle.

        Parameters
        ----------
        angle_degrees : float or int
            The central angle bounding the sector, in degrees.

        Returns
        -------
        float
            The area of the wedge-shaped sector.
        """
        self._validate_degrees(angle_degrees)
        return 0.5 * math.radians(angle_degrees) * self.radius ** 2
    
    # To calculate the segement area of a circle
    def segment_area(self, angle_degrees: float) -> float:
        """
        Calculate the area of a circular segment cut off by a straight chord.

        Parameters
        ----------
        angle_degrees : float or int
            The central angle forming the segment, in degrees. Must be 
            strictly between 0 and 180 degrees.

        Returns
        -------
        float
            The area of the circle segment.

        Raises
        ------
        TypeError
            If the angle is not an integer or a float.
        ValueError
            If the angle is not strictly within the interval (0, 180).
        """
        if not isinstance(angle_degrees, (int, float)):
            raise TypeError('Angle must be an integer or float')
        if angle_degrees <= 0 or angle_degrees >= 180:
            raise ValueError('Angle must be between 0 and 180 degrees to form a simple segment')
        
        total_slice = self.sector_area(angle_degrees)
        triangle = 0.5 * (self.radius ** 2) * math.sin(math.radians(angle_degrees))
        return total_slice - triangle
    
    # To calculate the chord length of a circle
    def chord_length(self, angle_degrees: float) -> float:
        """
        Calculate the linear length of a chord connecting two points on the arc.

        Parameters
        ----------
        angle_degrees : float or int
            The central angle subtending the chord, in degrees.

        Returns
        -------
        float
            The straight-line distance of the chord.
        """
        self._validate_degrees(angle_degrees)
        theta = math.radians(angle_degrees)
        return 2 * self.radius * math.sin(theta / 2)
    
    # To calculate the sagitta of a circle
    def sagitta_radians(self, angle_radians: float) -> float:
        """
        Calculate the sagitta height using a central angle measured in radians.

        The sagitta is the perpendicular distance from the center of the 
        chord to the highest point of the arc.

        Parameters
        ----------
        angle_radians : float or int
            The central angle, measured in radians. Must be between 0 and 2π.

        Returns
        -------
        float
            The height profile of the sagitta line segment.

        Raises
        ------
        TypeError
            If the angle is not an integer or a float.
        ValueError
            If the angle falls outside the closed interval [0, 2π].
        """
        if not isinstance(angle_radians, (int, float)):
            raise TypeError('Angle must be an integer or float')
        if angle_radians < 0 or angle_radians > (2 * math.pi):
            raise ValueError('Angle must be between 0 and 2*pi radians')

        return self.radius * (1 - math.cos(angle_radians / 2))

#---------------------------------------
#           Square - Child Class
#---------------------------------------
class Square(Shape2D):
    """
    A concrete implementation of a 2D shape representing a square.

    Provides geometric calculations for standard square metrics (area, perimeter, 
    diagonal length, circumradius, and centroid) and a utility method to 
    reverse-calculate length from a known area. It enforces strict type and 
    value validation on the side length.

    Parameters
    ----------
    length : float or int
        The side length of the square. Must be greater than zero.

    Attributes
    ----------
    length : float
        The validated side length of the square.
    name : str
        The identifying name of the shape, hardcoded to 'Square'.

    Raises
    ------
    TypeError
        If the provided length is not an integer or a float.
    ValueError
        If the provided length is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, length: float):
        super().__init__('Square')
        self.length = length

    @property
    def length(self) -> float:
        """
        float: The side length of the square. Enforces positive numeric constraints.
        """
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        if not isinstance(length, (int, float)):
            raise TypeError('Length must be an integer or float')
        if length <= 0:
            raise ValueError('Length must be greater than 0')
        self._length = length

    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the square.
        """
        return self._length * self._length
    
    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of all four sides) of the square.
        """
        return self._length * 4
    
    @property
    def diagonal(self) -> float:
        """
        float: The straight-line distance across the square from corner to corner.
        """
        return self._length * math.sqrt(2)
    
    @property
    def circumradius(self) -> float:
        """
        float: The radius of a circle that passes through all four vertices.
        """
        return self._length * math.sqrt(2) / 2
    
    @staticmethod
    def area_to_length(area: float) -> float:
        """
        Calculate the required side length of a square from its surface area.

        Parameters
        ----------
        area : float or int
            The total surface area. Must be greater than or equal to zero.

        Returns
        -------
        float
            The corresponding side length of the square.

        Raises
        ------
        TypeError
            If the provided area is not an integer or a float.
        ValueError
            If the area is a negative value.
        """
        if not isinstance(area, (int, float)):
            raise TypeError('Area must be an integer or float')
        if area < 0:
            raise ValueError('Area must be greater than or equal to 0')
        return math.sqrt(area)
    
    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are calculated relative to the bottom-left corner at (0, 0).
        """
        c = self._length / 2
        return c, c
  
#---------------------------------------
#           Rectangle - Child Class
#---------------------------------------
class Rectangle(Shape2D):
    """
    A concrete implementation of a 2D shape representing a rectangle.

    Provides geometric and engineering calculations for standard rectangle 
    metrics (area, perimeter, diagonal length, circumradius, and centroid) 
    as well as structural physics metrics like the second moment of area 
    and the intersecting angles of the diagonals. It enforces strict type 
    and value validation on both the length and height.

    Parameters
    ----------
    length : float or int
        The base length of the rectangle. Must be greater than zero.
    height : float or int
        The height of the rectangle. Must be greater than zero.

    Attributes
    ----------
    length : float
        The validated base length of the rectangle.
    height : float
        The validated height of the rectangle.
    name : str
        The identifying name of the shape, hardcoded to 'Rectangle'.

    Raises
    ------
    TypeError
        If either the provided length or height is not an integer or a float.
    ValueError
        If either the provided length or height is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, length: float, height: float):
        super().__init__('Rectangle')
        self.length = length
        self.height = height

    @property
    def length(self) -> float:
        """
        float: The base length of the rectangle. Enforces positive numeric constraints.
        """
        return self._length
    
    @length.setter
    def length(self, length: float) -> None:
        if not isinstance(length, (int, float)):
            raise TypeError('Length must be an integer or float')
        if length <= 0:
            raise ValueError('Length must be greater than 0')
        self._length = length

    @property
    def height(self) -> float:
        """
        float: The vertical height of the rectangle. Enforces positive numeric constraints.
        """
        return self._height
    
    @height.setter
    def height(self, height: float) -> None:
        if not isinstance(height, (int, float)):
            raise TypeError('Height must be an integer or float')
        if height <= 0:
            raise ValueError('Height must be greater than 0')
        self._height = height

    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the rectangle.
        """
        return self._length * self._height
    
    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of all four sides) of the rectangle.
        """
        return self._length * 2 + self._height * 2
    
    @property
    def diagonal(self) -> float:
        """
        float: The straight-line distance across the rectangle from corner to corner.
        """
        return math.sqrt(self._height ** 2 + self._length ** 2)
    
    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are calculated relative to the bottom-left corner at (0, 0).
        """
        cx = self._length / 2
        cy = self._height / 2
        return cx, cy
    
    @property
    def circumradius(self) -> float:
        """
        float: The radius of a circle that passes through all four vertices.
        """
        return (math.sqrt(self._length ** 2 + self._height ** 2)) / 2
    
    @property
    def second_moment_of_area(self) -> tuple[float, float]:
        """
        tuple of float: The area moments of inertia (Ix, Iy) about the centroidal axes.

        Returns
        -------
        ix : float
            The second moment of area relative to the horizontal x-axis.
        iy : float
            The second moment of area relative to the vertical y-axis.
        """
        ix = self._length * (self._height ** 3) / 12
        iy = self._height * (self._length ** 3) / 12
        return ix, iy
    
    @property
    def diagonal_angles(self) -> tuple[float, float]:
        """
        Calculate the two intersecting angles formed by the diagonals.

        Diagonals intersect to form two pairs of equal opposing angles. This 
        property automatically sorts the pairs to return the narrow 
        and wide angles respectively.

        Returns
        -------
        acute : float
            The acute intersection angle, in degrees.
        obtuse : float
            The obtuse intersection angle, in degrees.
        """
        # 1. Use math.atan() to find the angle in radians
        # 2. Convert it straight to degrees
        alpha = math.degrees(math.atan(self._height / self._length))

        # 3. Calculate both intersecting diagonal angles accurately
        angle_1 = 2 * alpha
        angle_2 = 180 - angle_1

        # 4. Sort them so you always know which one is acute vs obtuse
        acute = min(angle_1, angle_2)
        obtuse = max(angle_1, angle_2)

        return acute, obtuse
    
#---------------------------------------
#           Triangle - Child Classes
#---------------------------------------

class EquilateralTriangle(Shape2D):
    """
    A concrete implementation of a 2D shape representing an equilateral triangle.

    Provides geometric and engineering calculations for standard equilateral 
    triangle metrics (area, perimeter, height, inradius, circumradius, and 
    centroid) as well as structural physics metrics like the second moment of 
    area. It enforces strict type and value validation on the side length.

    Parameters
    ----------
    side : float or int
        The length of a single side of the triangle. Must be greater than zero.

    Attributes
    ----------
    side : float
        The validated side length of the triangle.
    name : str
        The identifying name of the shape, hardcoded to 'Equilateral Triangle'.

    Raises
    ------
    TypeError
        If the provided side length is not an integer or a float.
    ValueError
        If the provided side length is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, side: float):
        super().__init__('Equilateral Triangle')
        self.side = side

    @property
    def side(self) -> float:
        """
        float: The side length of the triangle. Enforces positive numeric constraints.
        """
        return self._side
    
    @side.setter
    def side(self, side: float) -> None:
        if not isinstance(side, (int, float)):
            raise TypeError('Side must be an integer or float')
        if side <= 0:
            raise ValueError('Side must be greater than 0')
        self._side = side
    
    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the equilateral triangle.
        """
        return (math.sqrt(3) / 4) * self._side ** 2
    
    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of all three equal sides).
        """
        return self._side * 3
    
    @property
    def inradius_property(self) -> float:
        """
        float: The radius of the largest circle that can fit inside the triangle.
        """
        return self._side / (2 * math.sqrt(3))
    
    @property
    def circumradius_property(self) -> float:
        """
        float: The radius of a circle that passes through all three vertices.
        """
        return self._side / math.sqrt(3)
    
    @property
    def height(self) -> float:
        """
        float: The perpendicular distance from any side to the opposite vertex.
        """
        return (math.sqrt(3) / 2) * self._side
    
    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are calculated relative to the bottom-left vertex at (0, 0)
        assuming the base sits flat along the x-axis.
        """
        cx = self._side / 2
        cy = self.height / 3
        return cx, cy
    
    @property
    def second_moment_of_area(self) -> tuple[float, float]:
        """
        tuple of float: The area moments of inertia (Ix, Iy) about the centroidal axes.

        Returns
        -------
        ix : float
            The second moment of area relative to the horizontal x-axis passing 
            through the centroid.
        iy : float
            The second moment of area relative to the vertical y-axis passing 
            through the centroid.
        """
        ix = (self._side * (self.height ** 3)) / 36
        iy = (self.height * (self._side ** 3)) / 48  
        return ix, iy

class RightAngleTriangle(Shape2D):
    """
    A concrete implementation of a 2D shape representing a right-angled triangle.

    Provides geometric and engineering calculations for standard right-angled 
    triangle metrics (area, hypotenuse, perimeter, angles, centroid, 
    circumradius, and inradius) as well as structural physics metrics like 
    the second moment of area. It enforces strict type and value validation 
    on both the base and height dimensions.

    Parameters
    ----------
    base : float or int
        The horizontal base length of the triangle. Must be greater than zero.
    height : float or int
        The vertical height of the triangle. Must be greater than zero.

    Attributes
    ----------
    base : float
        The validated base length of the triangle.
    height : float
        The validated height of the triangle.
    name : str
        The identifying name of the shape, hardcoded to 'Right Angle Triangle'.

    Raises
    ------
    TypeError
        If either the provided base or height is not an integer or a float.
    ValueError
        If either the provided base or height is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, base: float, height: float):
        super().__init__('Right Angle Triangle')
        self.base = base
        self.height = height
    
    @property
    def base(self) -> float:
        """
        float: The horizontal base length. Enforces positive numeric constraints.
        """
        return self._base
    
    @base.setter
    def base(self, base: float) -> None:
        if not isinstance(base, (int, float)):
            raise TypeError('Base must be an integer or float')
        if base <= 0:
            raise ValueError('Base must be greater than 0')
        self._base = base
    
    @property
    def height(self) -> float:
        """
        float: The vertical height length. Enforces positive numeric constraints.
        """
        return self._height
    
    @height.setter
    def height(self, height: float) -> None:
        if not isinstance(height, (int, float)):
            raise TypeError('Height must be an integer or float')
        if height <= 0:
            raise ValueError('Height must be greater than 0')
        self._height = height

    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the right-angled triangle.
        """
        return (0.5 * self._base) * self._height
    
    @property
    def hypotenuse(self) -> float:
        """
        float: The length of the longest side opposite the right angle.
        """
        return math.sqrt((self._base ** 2) + (self._height ** 2))
    
    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of the base, height, and hypotenuse).
        """
        return self._base + self._height + self.hypotenuse
    
    @property
    def angles(self) -> tuple[float, float, float]:
        """
        Calculate all three interior angles of the triangle in degrees.

        Returns
        -------
        tuple of float
            The three sorted interior angles in ascending order, including 
            the fixed 90.0-degree angle.
        """
        angle1 = math.degrees(math.atan(self._height / self._base))
        angle2 = 90 - angle1

        return tuple(sorted([90.0, angle1, angle2]))
    
    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are calculated relative to the right-angled vertex positioned 
        at the origin (0, 0).
        """
        cx = self._base / 3
        cy = self._height / 3
        return cx, cy
    
    @property
    def second_moment_of_area(self) -> tuple[float, float]:
        """
        tuple of float: The area moments of inertia (Ix, Iy) about the centroidal axes.

        Returns
        -------
        ix : float
            The second moment of area relative to the horizontal x-axis passing 
            through the centroid.
        iy : float
            The second moment of area relative to the vertical y-axis passing 
            through the centroid.
        """
        ix = (self._base * (self._height ** 3)) / 36
        iy = (self._height * (self._base ** 3)) / 36
        return ix, iy
    
    @property
    def circumradius(self) -> float:
        """
        float: The radius of a circle that passes through all three vertices.
        """
        return self.hypotenuse / 2
    
    @property
    def inradius(self) -> float:
        """
        float: The radius of the largest circle that can fit inside the triangle.
        """
        return ((self._base + self._height) - self.hypotenuse) / 2

class IsoscelesTriangle(Shape2D):
    """
    A concrete implementation of a 2D shape representing an isosceles triangle.

    Provides geometric and engineering calculations for standard isosceles 
    triangle metrics (area, height, perimeter, semi-perimeter, centroid, and 
    inradius) as well as structural physics metrics like the second moment of 
    area. It enforces strict type, value, and geometric validity validation 
    on both the base and equal side length dimensions.

    Parameters
    ----------
    base : float or int
        The horizontal base length of the triangle. Must be greater than zero.
    length : float or int
        The length of the two equal sides. Must be greater than half the base.

    Attributes
    ----------
    base : float
        The validated base length of the triangle.
    length : float
        The validated length of the two equal sides.
    name : str
        The identifying name of the shape, hardcoded to 'Isosceles Triangle'.

    Raises
    ------
    TypeError
        If either the provided base or length is not an integer or a float.
    ValueError
        If base or length is less than or equal to zero, or if length violates 
        geometric validity by being less than or equal to half the base.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, base: float, length: float):
        super().__init__('Isosceles Triangle')
        # We set length first, then base, so the validity check in base setter works smoothly during initialization
        self.length = length
        self.base = base
    
    @property
    def base(self) -> float:
        """
        float: The horizontal base length. Enforces positive numeric and geometric constraints.
        """
        return self._base
    
    @base.setter
    def base(self, base: float) -> None:
        if not isinstance(base, (int, float)):
            raise TypeError('Base must be an integer or float')
        if base <= 0:
            raise ValueError('Base must be greater than 0')
        if hasattr(self, '_length') and self._length <= base / 2:
            raise ValueError('Geometric invalidity: length must be greater than half the base')
        self._base = base
    
    @property
    def length(self) -> float:
        """
        float: The length of the two equal sides. Enforces positive numeric and geometric constraints.
        """
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        if not isinstance(length, (int, float)):
            raise TypeError('Length must be an integer or float')
        if length <= 0:
            raise ValueError('Length must be greater than 0')
        if hasattr(self, '_base') and length <= self._base / 2:
            raise ValueError('Geometric invalidity: length must be greater than half the base')
        self._length = length
    
    @property
    def height(self) -> float:
        """
        float: The perpendicular height from the base line to the apex vertex.
        """
        return math.sqrt(self._length**2 - ((self._base**2) / 4))
    
    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area of the isosceles triangle.
        """
        return (0.5 * self._base) * self.height

    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of the base and the two equal side lengths).
        """
        return (2 * self._length) + self._base
    
    @property
    def semi_perimeter(self) -> float:
        """
        float: Half of the total perimeter length used for incircle calculations.
        """
        return ((2 * self._length) + self._base) / 2 
    
    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are calculated relative to the midpoint of the base positioned 
        at the origin (0, 0).
        """
        cx = 0.0
        cy = self.height / 3
        return cx, cy
    
    @property
    def inradius(self) -> float:
        """
        float: The radius of the largest circle that can fit inside the triangle.
        """
        return self.area / self.semi_perimeter
    
    @property
    def second_moment_of_area(self) -> tuple[float, float]:
        """
        tuple of float: The area moments of inertia (Ix, Iy) about the centroidal axes.

        Returns
        -------
        ix : float
            The second moment of area relative to the horizontal x-axis passing 
            through the centroid.
        iy : float
            The second moment of area relative to the vertical axis of symmetry.
        """
        ix = (self._base * self.height**3) / 36
        iy = (self.height * self._base**3) / 48
        return ix, iy

class ScaleneTriangle(Shape2D):
    """
    A concrete implementation of a 2D shape representing a scalene triangle.

    Provides geometric and engineering calculations for standard scalene 
    triangle metrics (area, height, perimeter, semi-perimeter, centroid, and 
    inradius) as well as structural physics metrics like the second moment of 
    area. It enforces strict type, value, and geometric validation using the 
    triangle inequality theorem across all three unique side dimensions.

    Parameters
    ----------
    side_a : float or int
        The length of the first side of the triangle. Must be greater than zero.
    side_b : float or int
        The length of the second side of the triangle. Must be greater than zero.
    side_c : float or int
        The length of the third side of the triangle. Must be greater than zero.

    Attributes
    ----------
    side_a : float
        The validated length of the first side.
    side_b : float
        The validated length of the second side.
    side_c : float
        The validated length of the third side.
    name : str
        The identifying name of the shape, hardcoded to 'Scalene Triangle'.

    Raises
    ------
    TypeError
        If side_a, side_b, or side_c is not an integer or a float.
    ValueError
        If any side is less than or equal to zero, or if the side combinations 
        violate the triangle inequality theorem.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__('Scalene Triangle')
        # Initialize internal storage placeholders to bypass validation sequence issues
        self._side_a = 1.0
        self._side_b = 1.0
        self._side_c = 1.0
        
        # Sequentially trigger setters to execute validation checks fully
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_triangle(self, a: float, b: float, c: float) -> None:
        """Verify if three side segments physically form a valid closed triangle."""
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError('Geometric invalidity: The sum of any two sides must be strictly greater than the third side.')

    @property
    def side_a(self) -> float:
        """
        float: The length of the first side. Enforces positive numeric and structural constraints.
        """
        return self._side_a

    @side_a.setter
    def side_a(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError('Side A must be an integer or float')
        if value <= 0:
            raise ValueError('Side A must be greater than 0')
        self._validate_triangle(value, self._side_b, self._side_c)
        self._side_a = value

    @property
    def side_b(self) -> float:
        """
        float: The length of the second side. Enforces positive numeric and structural constraints.
        """
        return self._side_b

    @side_b.setter
    def side_b(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError('Side B must be an integer or float')
        if value <= 0:
            raise ValueError('Side B must be greater than 0')
        self._validate_triangle(self._side_a, value, self._side_c)
        self._side_b = value

    @property
    def side_c(self) -> float:
        """
        float: The length of the third side. Enforces positive numeric and structural constraints.
        """
        return self._side_c

    @side_c.setter
    def side_c(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError('Side C must be an integer or float')
        if value <= 0:
            raise ValueError('Side C must be greater than 0')
        self._validate_triangle(self._side_a, self._side_b, value)
        self._side_c = value

    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of all three distinct side lengths).
        """
        return self._side_a + self._side_b + self._side_c

    @property
    def semi_perimeter(self) -> float:
        """
        float: Half of the total perimeter length used for Heron's formula calculations.
        """
        return self.perimeter / 2

    @property
    def area(self) -> float:
        """
        float: The total cross-sectional area evaluated via Heron's Formula.
        """
        s = self.semi_perimeter
        return math.sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))

    @property
    def height(self) -> float:
        """
        float: The perpendicular height relative to side_a acting as the reference base.
        """
        return (2 * self.area) / self._side_a

    @property
    def centroid(self) -> tuple[float, float]:
        """
        tuple of float: The (x, y) coordinates representing the geometric centre.

        Coordinates are established by treating vertex A-B as a baseline aligned 
        at the coordinate plane origin.
        """
        # Place vertex 1 at (0,0) and vertex 2 at (side_c, 0)
        # Using law of cosines to find the 2D position of vertex 3 (cx, cy)
        x2 = self._side_c
        x3 = (self._side_c**2 + self._side_b**2 - self._side_a**2) / (2 * self._side_c)
        y3 = math.sqrt(abs(self._side_b**2 - x3**2))
        
        # Centroid is the average of coordinates: ((0 + x2 + x3)/3, (0 + 0 + y3)/3)
        cx = (x2 + x3) / 3
        cy = y3 / 3
        return cx, cy

    @property
    def inradius(self) -> float:
        """
        float: The radius of the largest circle that can fit inside the triangle.
        """
        return self.area / self.semi_perimeter

    @property
    def second_moment_of_area(self) -> tuple[float, float]:
        """
        tuple of float: The area moments of inertia (Ix, Iy) about the centroidal axes.

        Returns
        -------
        ix : float
            The second moment of area relative to the horizontal x-axis passing 
            through the centroid.
        iy : float
            The second moment of area relative to the vertical y-axis passing 
            through the centroid.
        """
        # Base horizontal width b is taken along side_a
        b = self._side_a
        h = self.height
        
        # Calculate projection offset to capture structural asymmetry along the horizontal plane
        alpha = math.sqrt(abs(self._side_b**2 - h**2))
        
        ix = (b * h**3) / 36
        iy = (b * h * (b**2 - b * alpha + alpha**2)) / 36
        return ix, iy

class TriangleFactory:
    """
    A factory class for dynamically instantiating various triangle types.

    This factory handles the mapping and creation of distinct 2D triangle 
    subclasses based on short-form string codes. It simplifies object creation 
    by routing layout configurations and dimensions through a centralized API.

    Attributes
    ----------
    processors : dict
        A class-level registry mapping shorthand string keys to their 
        corresponding concrete `Shape2D` triangle subclasses.
    """

    processors = {
        'ET': EquilateralTriangle,
        'RAT': RightAngleTriangle,
        'it': IsoscelesTriangle,
        'st': ScaleneTriangle
    }

    @staticmethod
    def create_triangle(triangle_type: str, **kwargs) -> Shape2D:
        """
        Instantiate a specific triangle subclass based on its type code.

        Parameters
        ----------
        triangle_type : str
            The key identifying the desired type of triangle. Accepted keys are:
            
            - 'ET' : EquilateralTriangle (requires `side`)
            - 'RAT' : RightAngleTriangle (requires `base`, `height`)
            - 'it' : IsoscelesTriangle
            - 'st' : ScaleneTriangle
        **kwargs : dict, optional
            Arbitrary keyword arguments passed directly to the targeted 
            triangle constructor for dimension validation and initialization.

        Returns
        -------
        Shape2D
            An instance of the requested concrete triangle subclass.

        Raises
        ------
        ValueError
            If the provided `triangle_type` code is not registered in the 
            `processors` dictionary.
        TypeError
            If the structural keyword arguments in `kwargs` do not match the 
            expected parameters of the targeted triangle's `__init__` constructor.
        """
        triangle_class = TriangleFactory.processors.get(triangle_type)
        if triangle_class:
            return triangle_class(**kwargs)
        else:
            raise ValueError(f'Unknown triangle type: {triangle_type}')

#---------------------------------------
#           Reg Pentagon - Child Class
#---------------------------------------
class Pentagon(Shape2D):

    """
    A concrete implementation of a 2D shape representing a Pentagon.

    Provides geometric and engineering calculations for standard pentagon
    metrics (area, height, perimeter, semi-perimeter, inradius, and circumradius) 
    as well as structural physics metrics like the second moment of 
    area. It enforces strict type, value, and geometric validity validation 
    on both the base and equal side length dimensions.

    Parameters
    ----------
    side : float or int
        The length of the pentagon. Must be greater than zero.
    
    Attributes
    ----------
    length : float
        The validated length of all sides.
    name : str
        The identifying name of the shape, hardcoded to 'Pentagon'.

    Raises
    ------
    TypeError
        If either the provided length is not an integer or a float.
    ValueError
        If length is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    def __init__(self, side):
        super().__init__('Pentagon')
        self.side = side
    
    @property
    def side(self) -> float:
        """
        float: The length of the pentagon. Enforces positive numeric constraints.
        """
        return self._side

    @side.setter
    def side(self, side: float) -> None:
        if not isinstance(side, (int , float)):
            raise TypeError('Side must be an integer or float')
        if side <= 0:
            raise ValueError('Side must be greater than 0')
        self._side = side
    
    @property
    def area(self) -> float:
        """
        float: The total amount of flat surface enclosed inside its five
        boundaries
        """
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self._side ** 2

    @property
    def perimeter(self) -> float:
        """
        float: The total perimeter (sum of all side lengths).
        """
        return 5 * self._side
    
    @property
    def inradius(self) -> float:
        """
        float: Is the radius of the internal circle that touches all
        five sides.
        """
        return self.perimeter / (10 * math.tan(math.radians(36)))
    
    @property
    def second_moment_of_area(self) -> float:
        """
        float: Measures how resistant a pentagonal cross-section is to 
        bending based entirely on its shape.
        """
        return 0.4851061955683935 * (self._side ** 4)
    
    
    @property
    def circumradius(self) -> float:
        """
        float: Is the distance from centre to any outer corner
        """
        return self._side / (2 * math.sin(math.radians(36)))           

#TODO next:
#---------------------------------------
#           Reg Hexagon - Child Class
#---------------------------------------
class Hexgaon(Shape2D):

    """
    A concrete implementation of a 2D shape representing a Hexagon.

    Provides geometric and engineering calculations for standard hexagon
    metrics (area, height, perimeter, inradius, and circumradius) 
    as well as structural physics metrics like the polar_moment_of_inertia. 
    It enforces strict type, value, and geometric validity validation on 
    both the base and equal side length dimensions.

    Parameters
    ----------
    side : float or int
        The length of the hexagon. Must be greater than zero.
    
    Attributes
    ----------
    length : float
        The validated length of all sides.
    name : str
        The identifying name of the shape, hardcoded to 'Hexagon'.

    Raises
    ------
    TypeError
        If either the provided length is not an integer or a float.
    ValueError
        If length is less than or equal to zero.

    See Also
    --------
    Shape2D : The parent abstract base class.
    """

    # Constructor method to initialise instance attributes
    def __init__(self, side: float):
        super().__init__('Hexagon')
        self.side = side

    @property
    def side(self) -> float:
        """
        float: The side of the hexagon. Enforces positive numeric constraints.
        """
        return self._side

    # Side error checking
    @side.setter
    def side(self, side: float) -> None:
        if not isinstance(side, (int, float)):
            raise TypeError('Side must be an integer or float')
        if side <= 0:
            raise ValueError('Side length must be greater than 0')
        self._side = side

    # Calculates the area of a hexagon
    @property
    def area(self) -> float:
        """
        float: Calculates the area of a regular hexagon given its 
        side length.
        """
        return (3 * math.sqrt(3) / 2) * (self._side ** 2)

    # Calculates the perimeter of a hexagon
    @property
    def perimeter(self) -> float:
        """
        float: Calculates the perimeter of a regular hexagon given 
        its side length.
        """
        return 6 * self._side

    # Calculates the longest diagonal (corner to corner)
    @property
    def longest_diagonal(self) -> float:
        """
        float: Calculates the longest diagonal (corner to corner)
        of the hexagon.

        Returns
        -------
            float: The length of the longest diagonal. 
        """
        return 2 * self._side

    # Calculates the shortest diagonal (flat to flat)
    @property
    def shortest_diagonal(self) -> float:
        """
        float: Calculates the shortest diagonal (flat to flat) of
        the hexagon.

        Returns
        -------
            float: The length of the shortest diagonal.
        """
        return self._side * math.sqrt(3)

    # Calculates the inradius of a hexagon
    @property
    def inradius(self) -> float:
        """
        float: Calculates the inradius (center to flat side) of 
        the hexagon.

        Returns
        -------
            float: The length of the inradius
        """
        return (self._side * math.sqrt(3)) / 2

    # Calculates the Polar Moment of Inertia
    @property
    def polar_moment_of_inertia(self) -> tuple[float, float, float]:
        """
        tuple: Calculates the inertia components and polar moment of inertia 
        of the hexagon using its side length.

        Returns
        -------
            tuple: A tuple containing (ix, iy, jz) as floats
        """
        ix = (5 * math.sqrt(3) / 16) * (self._side ** 4)

        iy = (5 * math.sqrt(3) / 16) * (self._side ** 4)

        jz = (5 * math.sqrt(3) / 8) * (self._side ** 4)

        return ix, iy, jz

    
# TODO: Next
#---------------------------------------
#           Reg Octagon - Child Class
#---------------------------------------







