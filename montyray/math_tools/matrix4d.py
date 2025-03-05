import numpy as np

from montyray.math_tools.vector4d import Vector4D
from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.point3d import Point3D


class Matrix4D:
    def __init__(self, mat4=None):
        if isinstance(mat4, Matrix4D):
            self._data = mat4._data
        elif isinstance(mat4, np.ndarray):
            self._data = mat4
        elif mat4 is None:
            self._data = np.array(np.identity(4, float))
        else:
            raise TypeError()

    @property
    def data(self):
        return self._data

    @property
    def determinant(self):
        return np.linalg.det(self._data)

    @property
    def inverse(self):
        return Matrix4D(np.linalg.inv(self._data))

    @property
    def transpose(self):
        return Matrix4D(np.transpose(self._data))

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other):
        if isinstance(other, Matrix4D):
            return np.array_equal(self._data, other._data)
        else:
            raise TypeError()

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other):
        if isinstance(other, Matrix4D):
            return Matrix4D(self._data + other._data)

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other):
        if isinstance(other, Matrix4D):
            return Matrix4D(self._data - other._data)
        else:
            raise TypeError()

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        if isinstance(other, Matrix4D):
            return self._mul(other)
        else:
            raise TypeError()

    def _mul(self, other):
        if isinstance(other, Matrix4D):
            return Matrix4D(np.matmul(self._data, other._data))
        elif isinstance(other, Vector4D):
            res = np.matmul(self._data, other.coordinates.reshape(4, 1))
            return Vector4D(res[0], res[1], res[2], res[3])
        elif isinstance(other, Vector3D):
            v4 = Vector4D(other)
            res = np.matmul(self._data, v4.coordinates.reshape(4, 1))
            return Vector3D(res[0, 0], res[1, 0], res[2, 0])
        elif isinstance(other, Point3D):
            v4 = Vector4D(other)
            res = np.matmul(self._data, v4.coordinates.reshape(4, 1))
            return Point3D(res[0, 0], res[1, 0], res[2, 0])
        else:
            raise TypeError()

    def __neg__(self):
        return Matrix4D(-self._data)

    def __abs__(self):
        return Matrix4D(np.abs(self._data))

    def __round__(self, n=None):
        return Matrix4D(np.round(self._data))

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col = key
            if row >= 0 and row <= 3 and col >= 0 and col <= 3:
                return self._data[row, col]
            else:
                raise IndexError()
        else:
            raise TypeError()

    def __setitem__(self, key, value):
        if isinstance(key, tuple) and isinstance(value, (int, float)):
            row, col = key
            if row >= 0 and row <= 3 and col >= 0 and col <= 3:
                self._data[row, col] = value
            else:
                raise IndexError()
        else:
            raise TypeError()
