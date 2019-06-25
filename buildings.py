"""
This file contains object definitions for modeling buildings.
"""
from common import *

class BuildingFactory:
    __metaclass__ = Singleton

    def NewArcherTower(self, lvl):
        """
        Arguments:
        """
        if lvl == 9:
            return DefenseBuilding(3, 3, hp=750, atk=56, range=10, dmg_type=DmgType.DMG_TYPE_GROUND,\
            dmg_target=DmgTargetType.DMG_TARGET_SINGLE)
        else:
            raise NotImplementedError()
        # TODO: Create more levels


class Building:
    def __init__(self, width, height, hp):
        """
        Arguments:
        """
        self.width = width
        self.height = height
        self.hp = hp

class DefenseBuilding(Building):
    def __init__(self, width, height, hp, atk, range, dmg_type, dmg_target):
        """
        Arguments:
        dmg_type: ground or air.
        dmg_target: single or splash
        """
        super().__init__(width, height, hp)
        self.atk = atk
        self.range = range
        self.dmg_type = dmg_type
        self.dmg_target = dmg_target

if __name__ == "__main__":
    cannon = DefenseBuilding(0, 4, 100, 5, 5, DmgType.DMG_TYPE_GROUND, DmgTargetType.DMG_TARGET_SINGLE)
