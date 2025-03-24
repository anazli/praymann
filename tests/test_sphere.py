# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.

import pytest
import numpy as np

from raymann.common.intersection import Intersection
from raymann.geometry.sphere import Sphere
from raymann.math_tools.math_utils import scale_matrix, translation_matrix
from raymann.math_tools.normal3d import Normal3D
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.ray import Ray
from raymann.math_tools.vector3d import Vector3D
from raymann.transformation.transformer import Transformer


class TestSphere:

    @pytest.mark.parametrize("transformation, origin, direction, t, is_intersect",
                             [(Transformer(),Point3D(0.0, 0.0, -5.0),Vector3D(0.0, 0.0, 1.0), 4, True),
                              (Transformer(),Point3D(0.0, 1.0, -5.0),Vector3D(0.0, 0.0, 1.0), 5, True),
                              (Transformer(),Point3D(0.0, 2.0, -5.0),Vector3D(0.0, 0.0, 1.0), np.inf, False),
                              (Transformer(),Point3D(0.0, 0.0, 0.0), Vector3D(0.0, 0.0, 1.0), 1,True),
                              (Transformer(scale_matrix(2.0, 2.0, 2.0)),Point3D(0.0, 0.0, -5.0), Vector3D(0.0, 0.0, 1.0), 3,True),
                              (Transformer(translation_matrix(5.0, 0.0, 0.0)),Point3D(0.0, 0.0, -5.0), Vector3D(0.0, 0.0, 1.0), 3,False),
                              ])

    def test_ray_sphere_intersection(self, transformation, origin, direction, t, is_intersect):
        sphere = Sphere(transformation)
        ray = Ray(origin=origin, direction=direction)
        record = Intersection()
        if is_intersect:
            assert sphere.intersect(ray, record)
            assert t == record.t_hit
        else:
            assert not sphere.intersect(ray, record)

    @pytest.mark.parametrize("point", [(Point3D(1, 0, 0)),
                                       (Point3D(0, 1,0)),
                                       (Point3D(0,0,1)),
                                       (Point3D(np.sqrt(3)/3,np.sqrt(3)/3,np.sqrt(3)/3))
                                       ])

    def test_sphere_normal(self, point):
        s = Sphere()
        n = s.normal(point)
        assert Normal3D(point) == n
        assert n.length() == 1.0