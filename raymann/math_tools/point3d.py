import numpy as np

from raymann.math_tools.vector3d import Vector3D


class Point3D:
    def __init__(self, *args):
        if len(args) == 3:
            if all(isinstance(val, (int, float, str, np.float64)) for val in args):
                self._data = np.array([args[0], args[1], args[2]], dtype=np.float64)
            else:
                raise TypeError("float,int or str must be provided for x,y,z")
        elif len(args) == 0:
            self._data = np.array([0, 0, 0])
        else:
            raise TypeError("Unknown type for Point3D initialization")

    @property
    def x(self) -> float:
        return self._data[0]

    @x.setter
    def x(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("float or int must be provided")
        self._data[0] = val

    @property
    def y(self) -> float:
        return self._data[1]

    @y.setter
    def y(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("float or int must be provided")
        self._data[1] = val

    @property
    def z(self) -> float:
        return self._data[2]

    @z.setter
    def z(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("float or int must be provided")
        self._data[2] = val

    @property
    def coordinates(self) -> np.ndarray:
        """returns the coordinates of a 3D point"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data: np.ndarray):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 3):
            raise TypeError()
        self._data = np.array(data)

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other: "Point3D") -> bool:
        if not isinstance(other, (Vector3D, Point3D)):
            raise TypeError("cannot compare Point3D with another type")
        return np.array_equal(self._data, other.coordinates)

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other: "int | float | Vector3D | Point3D") -> "Point3D | Vector3D":
        if isinstance(other, (float, int)):
            return Point3D(*(self._data + other))
        elif isinstance(other, Vector3D):
            return Vector3D(*(self._data + other.coordinates))
        elif isinstance(other, Point3D):
            return Point3D(*(self._data + other._data))
        else:
            raise TypeError("Unknown type for Point3D addition")

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other: "int | float | Vector3D | Point3D") -> "Point3D | Vector3D":
        if isinstance(other, (float, int)):
            return Point3D(*(self._data - other))
        elif isinstance(other, Point3D):
            return Vector3D(*np.subtract(self._data, other._data))
        elif isinstance(other, Vector3D):
            return Point3D(*np.subtract(self._data, other._data))
        else:
            raise TypeError("Unknown type for Point3D subtraction")

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other: "int | float | Point3D") -> "Point3D":
        if isinstance(other, (float, int)):
            return Point3D(*(self._data * other))
        elif isinstance(other, Point3D):
            return Point3D(*(self._data * other._data))
        else:
            raise TypeError("unknown type for Point3D multiplication")

    def __neg__(self) -> "Point3D":
        return Point3D(*(-self._data))

    def __abs__(self) -> "Point3D":
        return Point3D(*np.abs(self._data))

    def __str__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"
