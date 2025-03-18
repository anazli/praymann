# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
from raymann.math_tools.normal3d import Normal3D
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.vector3d import Vector3D


class Intersection:
    def __init__(self):
        self._hit_point = Point3D()
        self._normal = Normal3D()
        self._wo = Vector3D()
        self._surf_tangent = Vector3D()
        self._surf_bitangent = Vector3D()
        # Material of closest primitive
        # the closest primitive

    @property
    def hit_point(self):
        """The surface hit point in world coordinates"""
        return self._hit_point

    @hit_point.setter
    def hit_point(self, point):
        if isinstance(point, Point3D):
            self._hit_point = point
        else:
            raise TypeError("point should be provided")

    @property
    def normal(self):
        """The surface normal in world coordinates"""
        return self._normal

    @normal.setter
    def normal(self, n):
        if isinstance(n, Normal3D):
            self._normal = n
        else:
            raise TypeError("normal should be provided")

    @property
    def wo(self):
        """The ray's outgoing direction in world coordinates"""
        return self._wo

    @wo.setter
    def wo(self, v):
        if isinstance(v, Vector3D):
            self._wo = v

    @property
    def surf_tangent(self) -> Vector3D:
        return self._surf_tangent

    @surf_tangent.setter
    def surf_tangent(self, val:Vector3D):
        if isinstance(val, Vector3D):
            self._surf_tangent = val
        else:
            raise TypeError()

    @property
    def surf_bitangent(self) -> Vector3D:
        return self._surf_bitangent

    @surf_bitangent.setter
    def surf_bitangent(self, val: Vector3D):
        if isinstance(val, Vector3D):
            self._surf_bitangent = val
        else:
            raise TypeError()
