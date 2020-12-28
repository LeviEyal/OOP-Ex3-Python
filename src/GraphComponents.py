
class EdgeData(object):
    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.weight = w
        self.tag = 0

    def __repr__(self):
        return "({}->{})w:{:.3} ".format(self.src, self.dst, self.weight)


class GeoLocation(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def distance(self, other):
        t1 = (self.x - other.x) ** 2
        t2 = (self.y - other.y) ** 2
        t3 = (self.z - other.z) ** 2
        return (t1 + t2 + t3) ** 0.5


class NodeData(object):
    def __init__(self, key: int, tag=0, info="", location=GeoLocation(), weight=1):
        self.key = key
        self.tag = tag
        self.info = info
        self.location = GeoLocation(location[0], location[1], location[2])
        self.weight = weight

    def __repr__(self):
        # return "#{} tag:{} info:{} location:{} weight:{}".format(self.key, self.tag, self.info, self.location, self.weight)
        return "#{} pos:{} ".format(self.key, self.location)
