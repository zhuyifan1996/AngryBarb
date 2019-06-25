"""
This file contains unit test for map.
"""

import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from map import *
from buildings import BuildingFactory

class TestMap(unittest.TestCase):
    def SetUp(self):
        bf = BuildingFactory()
        tower = bf.NewArcherTower(lvl=9)
        map = Map(20, 20)
        map.AddBuilding(Point(1, 2), tower)

    def test_closest_empty_map(self):
        map = Map(20, 20)
        p, b = map.FindClosestBuilding(Point(5, 5))
        self.assertEqual(p, Point(0, 0))
        self.assertTrue(b is None)

if __name__ == '__main__':
    unittest.main()
