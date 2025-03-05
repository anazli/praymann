import numpy as np


class Vector2D:
    def __init__(self, *args):
        if len(args) == 2:
            if all(isinstance(val, (int, float, str, np.float64)) for val in args):
                self._data = np.array([args[0], args[1]], dtype=np.float64)
            else:
                raise TypeError()
        elif len(args) == 0:
            self._data = np.array([0, 0])
        else:
            raise TypeError()

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
    def coordinates(self):
        """returns the coordinates of a 2D vector"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 2):
            raise TypeError()
        self._data = np.array(data)

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError()
        return np.array_equal(self._data, other._data)

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other):
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data + other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self._data + other._data))
        else:
            raise TypeError()

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other):
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data - other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self._data - other._data))
        else:
            raise TypeError()

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other):
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data * other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self._data * other._data))
        else:
            raise TypeError()

    def __neg__(self):
        return Vector2D(*(-self._data))

    def __abs__(self):
        return Vector2D(*np.abs(self._data))

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def length(self):
        """length of a 2D vector"""
        return np.linalg.norm(self._data)

    def normalized(self):
        """returns the normalized vector"""
        return self._data / self.length()
