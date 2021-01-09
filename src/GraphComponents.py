# class EdgeData(object):
#     def __init__(self, src, dst, w):
#         self.src = src
#         self.dst = dst
#         self.w = w
#         self.tag = 0
#
#     def __repr__(self):
#         return "({}->{})w:{} ".format(self.src, self.dst, self.w)


class GeoLocation(object):
    def __init__(self, pos=None):
        self.pos = pos
        if pos is not None:
            self.x = pos[0]
            self.y = pos[1]
            self.z = pos[2]

    def __repr__(self):
        if self.pos is not None:
            return "{},{},{}".format(self.x, self.y, self.z)
        else:
            return "None"

    def distance(self, other):
        t1 = (self.x - other.x) ** 2
        t2 = (self.y - other.y) ** 2
        t3 = (self.z - other.z) ** 2
        return (t1 + t2 + t3) ** 0.5


class NodeData(object):
    def __init__(self, key: int, tag=0, info="", pos=None, weight=1):
        self.key = key
        self.tag = tag
        self.info = info
        self.weight = weight
        if pos is not None:
            self.position = pos
        else:
            self.position = None

    def __repr__(self):
        return "#{}".format(self.key)

    def __lt__(self, other):
        return self.tag < other.tag

    def __gt__(self, other):
        return self.tag > other.tag
