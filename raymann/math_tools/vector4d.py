# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np
from numpy.ma.core import nomask

from raymann.math_tools.vector3d import Vector3D
from raymann.math_tools.point3d import Point3D


class Vector4D:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Vector3D):
                self._data = np.append(args[0].coordinates, 0.0)
            elif isinstance(args[0], Point3D):
                self._data = np.append(args[0].coordinates, 1.0)
            else:
                raise TypeError("Vector3D, Point3D must be provided")
        elif len(args) == 4:
            if all(isinstance(val, (int, float, str, np.float64)) for val in args):
                self._data = np.array(
                    [args[0], args[1], args[2], args[3]], dtype=np.float64
                )
            else:
                raise TypeError("float,int or str must be provided for x,y,z,w")
        elif len(args) == 0:
            self._data = np.array([0, 0, 0, 0])
        else:
            raise TypeError("Unknown type was given")

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
    def w(self) -> float:
        return self._data[3]

    @w.setter
    def w(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError("float or int must be provided")
        self._data[3] = val

    @property
    def coordinates(self) -> np.ndarray:
        """returns the coordinates of a 4D vector"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data: np.ndarray):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 4):
            raise TypeError("numpy array must be provided")
        self._data = np.array(data)

    def __eq__(self, other):
        return _eq(other)

    def _eq(self, other: "Vector4D") -> bool:
        if not isinstance(other, Vector4D):
            raise TypeError("cannot compare Vector4D with other type")
        return np.array_equal(self._data, other._data)

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other: "Vector4D") -> "Vector4D":
        if isinstance(other, (float, int)):
            return Vector4D(*(self._data + other))
        elif isinstance(other, Vector4D):
            return Vector4D(*(self._data + other._data))
        else:
            raise TypeError("cannot add Vector4D to another type")

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other: "Vector4D") -> "Vector4D":
        if isinstance(other, (float, int)):
            return Vector4D(*(self._data - other))
        elif isinstance(other, Vector4D):
            return Vector4D(*np.subtract(self._data, other._data))
        else:
            raise TypeError("cannot do subtraction between Vector4D and another type")

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other: "int | float | Vector4D") -> "Vector4D":
        if isinstance(other, (float, int)):
            return Vector4D(*(self._data * other))
        elif isinstance(other, Vector4D):
            return Vector4D(*(self._data * other._data))
        else:
            raise TypeError()

    def __neg__(self) -> "Vector4D":
        return Vector4D(*(-self._data))

    def __abs__(self) -> "Vector4D":
        return Vector4D(*np.abs(self._data))

    def __str__(self) -> str:
        return f"Vector4D({self.x}, {self.y}, {self.z}, {self.w})"

    def length(self) -> float:
        """length of a 4D vector"""
        return np.linalg.norm(self._data)

    def normalized(self) -> "Vector4D":
        """returns the normalized vector"""
        norm_data = self._data / self.length()
        return Vector4D(norm_data[0], norm_data[1], norm_data[2], norm_data[3])
