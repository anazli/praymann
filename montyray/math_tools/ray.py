import numpy as np
from montyray.math_tools.point3d import Point3D
from montyray.math_tools.vector3d import Vector3D


class Ray:
    def __init__(self, *, origin, direction):
        if isinstance(origin, (np.ndarray, list)) and isinstance(
            direction, (np.ndarray, list)
        ):
            self._origin = Point3D(origin)
            self._direction = Vector3D(direction)
        elif isinstance(origin, Point3D) and isinstance(direction, Vector3D):
            self._origin = origin
            self._direction = direction
        else:
            raise TypeError(
                "Ray origin must be (ndarray, list, Point3D) and direction must be (ndarray, list, Vector3D"
            )

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction

    def position(self, t):
        return self._origin + t * self._direction
