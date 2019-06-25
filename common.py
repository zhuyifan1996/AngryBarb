from enum import Enum
import math

class DmgType(Enum):
    DMG_TYPE_UNKNOWN = 0
    DMG_TYPE_GROUND  = 1
    DMG_TYPE_AIR     = 2

class DmgTargetType(Enum):
    DMG_TARGET_UNKNOWN = 0
    DMG_TARGET_SINGLE = 1
    DMG_TARGET_SPLASH = 2

class BuildingTargetType(Enum):
    BUILDING_TYPE_UNKNOWN = 0
    BUILDING_TYPE_DEFENSE = 1
    BUILDING_TYPE_ALL     = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

"""
Metaclass for defining singleton classes.
"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
