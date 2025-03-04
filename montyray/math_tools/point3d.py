import numpy as np

from montyray.math_tools.vector3d import Vector3D


class Point3D:
    def __init__(self, *args):
        """initializes a vector from a numpy 3D array"""
        if len(args) == 1:
            if isinstance(args[0], (np.ndarray, list)) and len(args[0]) == 3:
                self._data = np.array(args[0])
            else:
                raise TypeError(
                    "A 3D numpy array or python list should be provided for Point3D initializiation"
                )
        elif len(args) == 3:
            if all(isinstance(val, (int, float)) for val in args):
                self._data = np.array([args[0], args[1], args[2]], dtype=np.float64)
            else:
                raise TypeError(
                    "Float variables (x,y,z) should be provided for Point3D initializiation"
                )
        elif len(args) == 0:
            self._data = np.array([0, 0, 0])
        else:
            raise TypeError("Unknown input type for Point3D initializiation")

    @property
    def x(self):
        return self._data[0]

    @x.setter
    def x(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[0] = val

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[1] = val

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[2] = val

    @property
    def coordinates(self):
        """returns the coordinates of a 3D point"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 3):
            raise TypeError()
        self._data = np.array(data)

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other):
        if not isinstance(other, (Vector3D, Point3D)):
            raise TypeError()
        return np.array_equal(self._data, other.coordinates)

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other):
        if not isinstance(other, (Point3D, float, int, Vector3D)):
            raise TypeError()
        if isinstance(other, (float, int)):
            return Point3D(self._data + other)
        elif isinstance(other, Vector3D):
            return Vector3D(self._data + other.coordinates)
        return Point3D(self._data + other._data)

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other):
        if not isinstance(other, (Point3D, float, int, Vector3D)):
            raise TypeError()
        if isinstance(other, (float, int)):
            return Point3D(self._data - other)
        elif isinstance(other, Point3D):
            return Vector3D(self._data - other._data)
        return Point3D(self._data - other._data)

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other):
        if not isinstance(other, (Point3D, float, int)):
            raise TypeError()
        if isinstance(other, (float, int)):
            return Point3D(self._data * other)
        return Point3D(self._data * other._data)

    def __neg__(self):
        return Point3D(-self._data)

    def __abs__(self):
        return Point3D(np.abs(self._data))

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
