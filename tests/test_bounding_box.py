import unittest
from raymann.math_tools.point3d import Point3D
from raymann.acceleration.bounding_box import BoundingBox

class TestBoundingBox(unittest.TestCase):

    def test_point_addition(self):
        p1 = Point3D(-5, 2, 0)
        p2 = Point3D(7, 0, -3)
        box = BoundingBox()
        box.add_point(p1)
        box.add_point(p2)
        self.assertEqual(Point3D(-5, 0, -3), box.min_point)
        self.assertEqual(Point3D(7, 2, 0), box.max_point)

    def test_box_addition(self):
        box1 = BoundingBox(Point3D(-5, -2, 0), Point3D(7, 4, 4))
        box2 = BoundingBox(Point3D(8, -7, -2), Point3D(14, 2, 8))
        box1.add_box(box2)
        self.assertEqual(Point3D(-5, -7, -2), box1.min_point)
        self.assertEqual(Point3D(14, 4, 8), box1.max_point)

    def test_box_contains_point(self):
        box = BoundingBox(Point3D(5, -2, 0), Point3D(11, 4, 7))
        self.assertTrue(box.contains_point(Point3D(5, -2, 0)))
        self.assertTrue(box.contains_point(Point3D(11, 4, 7)))
        self.assertTrue(box.contains_point(Point3D(8, 1, 3)))
        self.assertFalse(box.contains_point(Point3D(3, 0, 3)))
        self.assertFalse(box.contains_point(Point3D(8, -4, 3)))
        self.assertFalse(box.contains_point(Point3D(8, 1, -1)))
        self.assertFalse(box.contains_point(Point3D(13, 1, 3)))
        self.assertFalse(box.contains_point(Point3D(8, 5, 3)))
        self.assertFalse(box.contains_point(Point3D(8, 1, 8)))

    def test_box_contains_box(self):
        box1 = BoundingBox(Point3D(5, -2, 0), Point3D(11, 4, 7))
        box2 = BoundingBox(Point3D(5, -2, 0), Point3D(11, 4, 7))
        self.assertTrue(box1.contains_box(box2))
        box2 = BoundingBox(Point3D(6, -1, 1), Point3D(10, 3, 6))
        self.assertTrue(box1.contains_box(box2))
        box2 = BoundingBox(Point3D(4, -3, -1), Point3D(10, 3, 6))
        self.assertFalse(box1.contains_box(box2))
        box2 = BoundingBox(Point3D(6, -1, 1), Point3D(12, 5, 8))
        self.assertFalse(box1.contains_box(box2))



