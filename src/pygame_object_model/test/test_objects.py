import unittest
import sys
sys.path.append("..")
from object import Object
from point import Point

class Test_Object(unittest.TestCase):
    def test_collisions(self):
        object1 = Object(Point(0,0), Point(10,10), "o1")
        object2 = Object(Point(0,0), Point(10,10), "02")
        
        def check_collision(object1: Object, object2: Object, loc1: list, loc2: list, expect_collision):
            for index, _ in enumerate(loc1):
                object1.Location = Point(loc1[index][0], loc1[index][1])
                object2.Location = Point(loc2[index][0], loc2[index][1])
                self.assertEqual(object1.is_colliding_basic(object2), expect_collision)

        # Test barely touching
        check_collision(object1, object2,
            [(0,0),(0,0),(0,0),(0,0)],
            [(-9,-9),(0,10),(10,0),(10,10)],
            True)
        
        # Test barely no touch
        check_collision(object1, 
            object2, 
            [(0,0),(0,0),(11,0)],
            [(11,0),(10,11),(0,0)], 
            False)

