# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np

from raymann.math_tools.point3d import Point3D
from raymann.math_tools.ray import Ray


class BoundingBox:
    def __init__(
        self,
        min_point: Point3D = Point3D(np.inf, np.inf, np.inf),
        max_point: Point3D = Point3D(-np.inf, -np.inf, -np.inf),
    ):
        if isinstance(min_point, Point3D) and isinstance(max_point, Point3D):
            self._min_point = min_point
            self._max_point = max_point
        else:
            raise TypeError(
                "invalid parameters for bbox initialization, must be Point3D"
            )

    @property
    def min_point(self) -> Point3D:
        return self._min_point

    @min_point.setter
    def min_point(self, point: Point3D):
        if isinstance(point, Point3D):
            self._min_point = point
        else:
            raise TypeError("must be Point3D")

    @property
    def max_point(self) -> Point3D:
        return self._max_point

    @max_point.setter
    def max_point(self, point: Point3D):
        if isinstance(point, Point3D):
            self._max_point = point
        else:
            raise TypeError("must be Point3D")

    def add_point(self, point: Point3D):
        if isinstance(point, Point3D):
            if point.x < self._min_point.x:
                self._min_point.x = point.x
            if point.y < self._min_point.y:
                self._min_point.y = point.y
            if point.z < self._min_point.z:
                self._min_point.z = point.z

            if point.x > self._max_point.x:
                self._max_point.x = point.x
            if point.y > self._max_point.y:
                self._max_point.y = point.y
            if point.z > self._max_point.z:
                self._max_point.z = point.z
        else:
            raise TypeError("cannot add unknown type to BBox")

    def add_box(self, box: "BoundingBox"):
        if isinstance(box, BoundingBox):
            self.add_point(box.min_point)
            self.add_point(box.max_point)
        else:
            raise TypeError("cannot add unknown type to BBox")

    def contains_point(self, point: Point3D) -> bool:
        if isinstance(point, Point3D):
            return (
                point.x >= self._min_point.x
                and point.x <= self._max_point.x
                and point.y >= self._min_point.y
                and point.y <= self.max_point.y
                and point.z >= self._min_point.z
                and point.z <= self._max_point.z
            )
        return False

    def contains_box(self, box: "BoundingBox") -> bool:
        if isinstance(box, BoundingBox):
            return self.contains_point(box.min_point) and self.contains_point(
                box.max_point
            )
        return False

    def intersects_ray(self, ray: Ray) -> bool:
        if not isinstance(ray, Ray):
            raise TypeError("ray needed as parameter")
        o = ray.origin
        d = ray.direction
        xminmax = self._hit_axis(o.x, d.x, self.min_point.x, self.min_point.x)
        yminmax = self._hit_axis(o.y, d.y, self.min_point.y, self.min_point.y)
        zminmax = self._hit_axis(o.z, d.z, self.min_point.z, self.min_point.z)
        tmin = max(max(xminmax[0], yminmax[0]), zminmax[0])
        tmax = min(min(xminmax[1], yminmax[1]), zminmax[1])
        if tmin > tmax:
            return False
        return True

    def _hit_axis(
        self,
        origin: int | float,
        direction: int | float,
        mmin: int | float,
        mmax: int | float,
    ) -> (float, float):
        tmin_numer = mmin - origin
        tmax_numer = mmax - origin
        tmin, tmax = 0, 0
        if abs(direction) >= 0.00001:
            tmin = tmin_numer / direction
            tmax = tmax_numer / direction
        else:
            tmin = tmin_numer * np.inf
            tmax = tmax_numer * np.inf

        if tmin > tmax:
            tmin, tmax = tmax, tmin

        return tmin, tmax
