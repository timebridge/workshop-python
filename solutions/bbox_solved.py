# -*- coding: utf-8 -*-


class Bbox(object):
    def __init__(self, north, south, east, west):
        """
        (N, W)           (N, E)
          +----------------+
          |                |
          +----------------+
        (S, W)           (S, E)

                        N,  S,  E, W

        >>> bbox = Bbox(10, 0, 10, 0)
        >>> bbox.north
        10
        >>> bbox.south
        0
        >>> bbox.east
        10
        >>> bbox.west
        0
        """
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __repr__(self):
        """Return the python representation

        >>> bbox = Bbox(10, 0, 10, 0)
        >>> bbox
        Bbox(10, 0, 10, 0)
        """
        return "Bbox(%r, %r, %r, %r)" % (self.north, self.south,
                                         self.east, self.west)

    def __add__(self, addend):
        """
        (N0, W0)        (N0, E0)
          +-----------------+~~~~~+
          |                 |     !
          |                 |     !
          |     (N1, W1)    |  (N1, E1)
          |        +--------|-----+
          |        |        |     |
          +-----------------+     |
        (S0, W0)   |     (S0, E0) |
          !        |              |
          !        |              |
          !        |              |
          !        |              |
          +~~~~~~~~+--------------+
                (S1, W1)       (S1, E1)


        >>> bbox0 = Bbox(12, 6, 18, 0)
        >>> bbox1 = Bbox( 8, 0, 24, 7)
        >>> bbox0 + bbox1
        Bbox(12, 0, 24, 0)
        """
        north = max([self.north, addend.north])
        south = min([self.south, addend.south])
        east = max([self.east, addend.east])
        west = min([self.west, addend.west])
        return Bbox(north, south, east, west)

    def __sub__(self, subtracting):
        """
        (N0, W0)        (N0, E0)
          +-----------------+~~~~~+
          |                 |     !
          |                 |     !
          |     (N1, W1)    |  (N1, E1)
          |        +--------|-----+
          |        |        |     |
          +-----------------+     |
        (S0, W0)   |     (S0, E0) |
          !        |              |
          !        |              |
          !        |              |
          !        |              |
          +~~~~~~~~+--------------+
                (S1, W1)       (S1, E1)


        >>> bbox0 = Bbox(12, 6, 18, 0)
        >>> bbox1 = Bbox( 8, 0, 24, 7)
        >>> bbox0 - bbox1
        Bbox(8, 6, 18, 7)
        """
        north = min([self.north, subtracting.north])
        south = max([self.south, subtracting.south])
        east = min([self.east, subtracting.east])
        west = max([self.west, subtracting.west])
        return Bbox(north, south, east, west)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)