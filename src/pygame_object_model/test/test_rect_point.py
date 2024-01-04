import unittest
import sys
sys.path.append("..")
from rect import Rect
from point import Point

class Test_Rect(unittest.TestCase):
    def test_rect_intersection(self):
        def check_intersection(loc1: list, loc2: list, expected: list):
            for index, _ in enumerate(loc1):
                #print(Point(*loc1[index]))
                r1 = Rect(Point(*loc1[index]),Point(10,10))
                r2 = Rect(Point(*loc2[index]),Point(10,10))
                ex = Rect.from_points(*expected[index])
                intersection = r1.intersection(r2)
                #print(f"R1[{r1}] R2[{r2}] Expected[{ex}] Intersection[{intersection}]")
                self.assertEqual(str(intersection), str(ex))
        check_intersection(
            # Location of Object1
            [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
            # Location of Object2
            [(0,0),(5,5),(9,9),(0,9),(-9,0),(0,-9),(11,11)],
            # Expected points of intersection
            [(0,0,10,10),(5,5,10,10),(9,9,10,10),(0,9,10,10),(0,0,1,10),(0,0,10,1),(0,0,0,0)]
        )

        bug_r1 = Rect(Point(600,500),Point(5,5))
        bug_r2 = Rect(Point(765, 80), Point(30,20))
        intersection = bug_r1.intersection(bug_r2)
        print(f"Intersection: {intersection}")

    def test_point_slope(self):
        def check_slope(p1: list, p2: list, expected: list):
            for index, _ in enumerate(p1):
                self.assertEqual(str(Point(*p1[index]).get_slope(Point(*p2[index]))), str(Point(*expected[index]))) 
        check_slope(
            [(0,0),(0,0),(0,0)],
            [(1,1),(-1,-1),(1,0)],
            [(1,1),(-1,-1),(1,0)],
        )