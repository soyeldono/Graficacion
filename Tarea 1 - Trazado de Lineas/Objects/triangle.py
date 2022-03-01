from .line import Line

class Triangle:
    idTriangle = -1

    def __init__(self, p0, p1, p2, name=""):
        type(self).idTriangle += 1
        self.p0 = p0
        self.x0 = p0[0]
        self.y0 = p0[1]
        self.p1 = p1
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.p2 = p2
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.lines = []
        self.points = []
        self.name = name if name != "" else f"Triangle {self.idTriangle}"
    
    def calculate(self):
        self.lines = [Line(self.p0,self.p1),Line(self.p1,self.p2),Line(self.p2,self.p0)]

        for l in self.lines:
            l.calculate()
            for c in l.points:
                self.points.append(c)