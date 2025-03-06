import numpy as np


class Vector3D:
    def __init__(self, *args):
        if len(args) == 3:
            if all(isinstance(val, (int, float, str, np.float64)) for val in args):
                self._data = np.array([args[0], args[1], args[2]], dtype=np.float64)
            else:
                raise TypeError("float,int or str must be provided for x,y,z")
        elif len(args) == 0:
            self._data = np.array([0, 0, 0])
        else:
            raise TypeError("Unknown type for Vector3D initialization")

    @property
    def x(self) -> float:
        return self._data[0]

    @x.setter
    def x(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[0] = val

    @property
    def y(self) -> float:
        return self._data[1]

    @y.setter
    def y(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[1] = val

    @property
    def z(self) -> float:
        return self._data[2]

    @z.setter
    def z(self, val: int | float):
        if not isinstance(val, (int, float)):
            raise TypeError()
        self._data[2] = val

    @property
    def coordinates(self) -> np.ndarray:
        """returns the coordinates of a 3D vector"""
        return self._data.copy()

    @coordinates.setter
    def coordinates(self, data: np.ndarray):
        if not (isinstance(data, (np.ndarray, list)) and len(data) == 3):
            raise TypeError("A numpy array must be provided")
        self._data = np.array(data)

    def __eq__(self, other):
        return self._eq(other)

    def __req__(self, other):
        return self._eq(other)

    def _eq(self, other: "Vector3D") -> bool:
        if isinstance(other, Vector3D):
            return np.array_equal(self._data, other._data)
        else:
            raise TypeError("cannot compare Vector3D with another type")

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def _add(self, other: "int | float | Vector3D") -> "Vector3D":
        if not isinstance(other, (Vector3D, float, int)):
            raise TypeError("cannot add Vector3D to another type")
        if isinstance(other, (float, int)):
            return Vector3D(*(self._data + other))
        return Vector3D(*(self._data + other._data))

    def __sub__(self, other):
        return self._sub(other)

    def __rsub__(self, other):
        return self._sub(other)

    def _sub(self, other: "int | float | Vector3D") -> "Vector3D":
        if not isinstance(other, (Vector3D, float, int)):
            raise TypeError("cannot do subtraction between Vector3D and another type")
        if isinstance(other, (float, int)):
            return Vector3D(*(self._data - other))
        return Vector3D(*(self._data - other._data))

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def _mul(self, other: "int | float | Vector3D") -> "Vector3D":
        if not isinstance(other, (Vector3D, float, int)):
            raise TypeError(
                "cannot do multiplication between Vector3D and another type"
            )
        if isinstance(other, (float, int)):
            return Vector3D(*(self._data * other))
        return Vector3D(*(self._data * other._data))

    def __neg__(self) -> "Vector3D":
        return Vector3D(*(-self._data))

    def __abs__(self) -> "Vector3D":
        return Vector3D(*np.abs(self._data))

    def __str__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def length(self) -> float:
        """length of a 3D vector"""
        return np.linalg.norm(self._data)

    def normalized(self) -> "Vector3D":
        """returns the normalized vector"""
        return self._data / self.length()
