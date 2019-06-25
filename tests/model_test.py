"""
This file contains unit test for object definitions for troops, buildings,
"""

import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from buildings import *
from troops import *

class TestTroops(unittest.TestCase):
    def test_does_compile(self):
        minion1 = Troop(10, 100, 10, 1, DmgType.DMG_TYPE_GROUND, BuildingTargetType.BUILDING_TYPE_ALL)

class TestBuildings(unittest.TestCase):
    def test_does_compile(self):
        cannon = DefenseBuilding(0, 4, 100, 5, 5, DmgType.DMG_TYPE_GROUND, DmgTargetType.DMG_TARGET_SINGLE)

    def test_factory_archer_tower(self):
        bf = BuildingFactory()
        tower = bf.NewArcherTower(lvl=9)

if __name__ == '__main__':
    unittest.main()
