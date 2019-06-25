"""
Map contains organizes a collection of buildings (including their coordinates)
and acts as the defensive end of a simulation.
"""
from common import Point

class Map:
    def __init__(self, width, height):
        """
        buildings: a list of (ul:Point, b:Building) tuples. ul is the upper-left
            corner of the building, b is the building.
        """
        self.width = width
        self.height = height
        self.buildings = []

    def AddBuilding(self, ul, building):
        self.buildings.append((ul, building))
        self.Validate()

    def FindClosestBuilding(self, point):
        """
        Returns a (Point, Building) representing the closest building from point.
        If no building is present, return ((0, 0), None)
        """
        closest, nearest_b, min_dist = Point(0, 0), None, 1e6
        for ul, b in self.buildings:
            dist = ul.dist(point)
            if (min_dist > dist):
                closest = ul
                nearest_b = b
        return closest, nearest_b

    def Validate(self):
        """
        Validate if the current buildings have any overlap, or if any building
        is out of bound.
        Throws exception if validation fails.
        """
        pass
