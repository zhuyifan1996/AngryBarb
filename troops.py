"""
This file contains object definitions for modeling army.
"""
from common import *

class Troop:
    def __init__(self, atk, hp, speed, housing_space, dmg_type, favored_target):
        """
        Arguments:
        atk:   damage per second
        hp:    hitpoint
        speed: num of squares the unit can move per second
        ...
        """
        self.atk = atk
        self.hp = hp
        self.speed = speed
        self.housing_space = housing_space
        self.dmg_type = dmg_type
        self.favored_target = favored_target


if __name__ == "__main__":
    minion1 = Troop(10, 100, 10, 1, DmgType.DMG_TYPE_GROUND, BuildingTargetType.BUILDING_TYPE_ALL)
