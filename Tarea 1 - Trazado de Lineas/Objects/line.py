#__file__ = "../screen"

#from screen import Pixel

class Line:
    idLine = -1
    def __init__(self, p0, p1, ltype='dda', name="") -> None:
        type(self).idLine += 1
        self.ltype = ltype
        self.p0 = p0
        self.x0 = p0[0]
        self.y0 = p0[1]
        self.p1 = p1
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.points = [(self.x0,self.y0)]
        self.name = name if name != "" else f"Line {self.idLine}"
        self.pixels = []
    

    def calculate(self):
        if self.ltype == 'dda':
            mx = self.x1 - self.x0
            my = self.y1 - self.y0
            s = abs(mx) if abs(mx) > abs(my) else abs(my)

            Dx = mx/s
            Dy = my/s

            x = self.x0
            y = self.y0

            self.points.append((int(x),int(y)))

            for _ in range(s-1):
                x = x + Dx
                y = y + Dy
                self.points.append((int(x),int(y)))
            
            self.points.append((self.x1,self.y1))
    

                    

