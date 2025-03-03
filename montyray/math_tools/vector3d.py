import numpy as np


class Vector3D:
    def __init__(self, data):
        """initializes a vector from a numpy 3D array"""
        if not isinstance(data, np.ndarray):
            raise TypeError(
                "Numpy array should be provided for Vector3D initializiation"
            )
        if not len(data) == 3:
            raise ValueError("Wrong dimension for Vector3D data")
        self._data = data

    def __init__(self, x, y, z):
        """initializes a vector from 3 coordinates"""
        self._data = np.array([x, y, z], dtype=np.float64)

    @property
    def x(self):
        return self._data[0]

    @x.setter
    def x(self, val):
        self._data[0] = val

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, val):
        self._data[1] = val

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, val):
        self._data[2] = val

    @property
    def coordinates(self):
        """returns the coordinates of a 3D vector"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data):
        self._data = data.copy()

    def __add__(self, other):
        """adds two 3D vectors"""
        return Vector3D(self._data + other._data)

    def __sub__(self, other):
        """subtracts two 3D vectors"""
        return Vector3D(self._data - other._data)

    def __mul__(self, other):
        """multiplies two 3D vectors"""
        return Vector3D(self._data * other._data)

    def __neg__(self):
        """negetion of 3D vector"""
        return Vector3D(-self._data)

    def __abs__(self):
        """absolute value of a 3D vector"""
        return Vector3D(np.abs(self._data))

    def __str__(self):
        """string representation of a 3D vector"""
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def length(self):
        """length of a 3D vector"""
        return np.linalg.norm(self._data)
