# Copyright (c) 2025 Andreas Nazlidis
# Licensed under the GNU General Public License v3.
# See LICENSE file for details.

import unittest
import numpy as np

from raymann.common.intersection import Intersection
from raymann.geometry.sphere import Sphere
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.ray import Ray
from raymann.math_tools.vector3d import Vector3D


class TestSphere(unittest.TestCase):

    def test_ray_sphere_intersection(self):
        sphere = Sphere()
        ray = Ray(origin=Point3D(0.0, 0.0, -5.0), direction=Vector3D(0.0, 0.0, 1.0))
        record = Intersection()
        self.assertTrue(sphere.intersect(ray, record))
        self.assertEqual(4, record.t_hit)
