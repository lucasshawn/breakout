import unittest
import sys
sys.path.append("..")
from object import Object
from point import Point
from rect import Rect

class Test_Object(unittest.TestCase):
    def test_collisions(self):
        def check_collision_old(loc1: list, loc2: list, expect_collision):
            for index, _ in enumerate(loc1):
                #print(Point(*loc2[index]))
                object1 = Object(Point(*(loc1[index])), Point(10,10), "o1")
                object2 = Object(Point(*(loc2[index])), Point(10,10), "o2")
                self.assertEqual(object1.is_colliding_basic(object2), expect_collision)
        
        def check_collision(loc1: list, loc2: list, expected: list):
            for index, _ in enumerate(loc1):
                object1 = Object(Point(*(loc1[index])), Point(10,10), "o1")
                object2 = Object(Point(*(loc2[index])), Point(10,10), "o2")
                (collided, collision_rect, slope) = object1.get_collision_details(object2)
                print("-----")
                print(collided)
                print(collision_rect)
                print(slope)
                print("-----")
                
        check_collision(
            [(0,0)],
            [(-9,-9)],
            [(True, Rect.from_points(0,0,1,10), Point(1,1))]
        )
             
        # check_collision(
        #     [(0,0),(0,0),(0,0),(0,0)],
        #     [(-9,-9),(0,10),(10,0),(10,10)],
        #     [(True, Rect.from_points(0,0,1,10))
        
        # # Test barely no touch
        # check_collision([(0,0),(0,0),(11,0)],
        #     [(11,0),(10,11),(0,0)], 
        #     False)

