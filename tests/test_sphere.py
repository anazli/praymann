# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.

import pytest

from raymann.common.intersection import Intersection
from raymann.geometry.sphere import Sphere
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.ray import Ray
from raymann.math_tools.vector3d import Vector3D


class TestSphere:

    @pytest.mark.parametrize("origin, direction, thit",
                             [(Point3D(0.0, 0.0, -5.0),Vector3D(0.0, 0.0, 1.0), 4),
                              (Point3D(0.0, 0.0, -5.0),Vector3D(0.0, 0.0, 1.0), 4),
                              (Point3D(0.0, 0.0, -5.0),Vector3D(0.0, 0.0, 1.0), 4)])

    def test_ray_sphere_intersection(self, origin, direction, thit):
        sphere = Sphere()
        ray = Ray(origin=origin, direction=direction)
        record = Intersection()
        assert sphere.intersect(ray, record)
        assert thit == record.t_hit