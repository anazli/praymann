# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np


class Vector2D:
    def __init__(self, *args):
        if len(args) == 2:
            if all(isinstance(val, (int, float, str, np.float64)) for val in args):
                self._data = np.array([args[0], args[1]], dtype=np.float64)
            else:
                raise TypeError(
                    "int, float or str must be provided for Vector2D initialization"
                )
        elif len(args) == 0:
            self._data = np.array([0, 0])
        else:
            raise TypeError("Unknown type for Vector2D initialization")

    @property
    def x(self) -> float:
        return self._data[0]

    @x.setter
    def x(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("int or float must be provided")
        self._data[0] = val

    @property
    def y(self) -> float:
        return self._data[1]

    @y.setter
    def y(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("int or float must be provided")
        self._data[1] = val

    @property
    def coordinates(self) -> np.ndarray:
        """returns the coordinates of a 2D vector"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data: np.ndarray):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 2):
            raise TypeError("numpy array must be provided")
        self._data = np.array(data)

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("cannot compare Vector2D with another type")
        return np.array_equal(self._data, other._data)

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other: "Vector2D") -> "Vector2D":
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data + other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self._data + other._data))
        else:
            raise TypeError("cannot add Vector2D to another type")

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other: "Vector2D") -> "Vector2D":
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data - other))
        elif isinstance(other, Vector2D):
            return Vector2D(*np.subtract(self._data, other._data))
        else:
            raise TypeError("cannot do subtraction between Vector2D and another type")

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other: "Vector2D") -> "Vector2D":
        if isinstance(other, (float, int)):
            return Vector2D(*(self._data * other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self._data * other._data))
        else:
            raise TypeError("cannot multiply Vector2D with another type")

    def __neg__(self) -> "Vector2D":
        return Vector2D(*(-self._data))

    def __abs__(self) -> "Vector2D":
        return Vector2D(*np.abs(self._data))

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def length(self) -> float:
        """length of a 2D vector"""
        return np.linalg.norm(self._data)

    def normalized(self) -> "Vector2D":
        """returns the normalized vector"""
        norm_data = self._data / self.length()
        return Vector2D(norm_data[0], norm_data[1])
