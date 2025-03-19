# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.
import numpy as np

from raymann.geometry.primitive import Primitive, get_min_hit_param
from raymann.math_tools.math_utils import dot
from raymann.math_tools.normal3d import Normal3D
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.vector3d import Vector3D
from raymann.transformation.transformer import Transformer
from raymann.math_tools.ray import Ray
from raymann.common.intersection import Intersection


class Sphere(Primitive):
    def __init__(
        self,
        transf: Transformer = Transformer(),
        center: Point3D = Point3D(),
        radius: int | float = 1.0,
    ):
        if (
            isinstance(transf, Transformer)
            and isinstance(center, Point3D)
            and isinstance(radius, (int, float))
        ):
            super().__init__(transf)
            self._center = center
            self._radius = radius
        else:
            raise TypeError("invalid input for sphere, should be (Point3D, int|float)")

        self._bbox.min_point = Point3D(-1, -1, -1) + self._center
        self._bbox.max_point = Point3D(1, 1, 1) + self._center

    def intersect(self, ray: Ray, record: Intersection) -> bool:
        super().intersect(ray, record)
        transf_ray = self._transformation.world_to_obj_space(ray)
        o = transf_ray.origin
        d = transf_ray.direction
        co = o - self._center
        a = dot(d, d)
        b = 2.0 * dot(d, co)
        c = dot(co, co) - self._radius**2
        discr = b**2 - 4.0 * a * c
        if discr >= 0.0:
            t1 = (-b - np.sqrt(discr)) / (2.0 * a)
            t2 = (-b + np.sqrt(discr)) / (2.0 * a)
            record.t_hit = get_min_hit_param(transf_ray.tmin, transf_ray.tmax, t1, t2)
            record.hit_point.coordinates = transf_ray.position(record.t_hit).coordinates
            record.wo = -ray.direction # in world coords
            record.normal = Normal3D((record.hit_point - self._center).normalized())
            return True
        return False

    def pdf(self, record: Intersection, wi: Vector3D) -> float:
        pass

    def surface_area(self) -> float:
        return 4.0 * np.pi * self._radius**2
