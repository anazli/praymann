# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.vector3d import Vector3D


class Ray:
    def __init__(
        self,
        *,
        origin: Point3D,
        direction: Vector3D,
        tmin: float = 0.001,
        tmax: float = np.inf
    ):
        self._tmin = tmin
        self._tmax = tmax
        if isinstance(origin, (np.ndarray, list)) and isinstance(
            direction, (np.ndarray, list)
        ):
            self._origin = Point3D(*origin)
            self._direction = Vector3D(*direction)
        elif isinstance(origin, Point3D) and isinstance(direction, Vector3D):
            self._origin = origin
            self._direction = direction
        else:
            raise TypeError(
                "Ray origin must be (ndarray, list, Point3D) and direction must be (ndarray, list, Vector3D"
            )

    @property
    def origin(self) -> Point3D:
        return self._origin

    @property
    def direction(self) -> Vector3D:
        return self._direction

    @property
    def tmin(self) -> float:
        return self._tmin

    @property
    def tmax(self) -> float:
        return self._tmax

    def position(self, t) -> Vector3D:
        return self._origin + t * self._direction
