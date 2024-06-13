class point:
    points(0,10)

    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def pointsss(point):
        match point:
            case point(x=0,y=0):
                print("Orign")
            case point(x=0,y=y):
                print(f"{point.y}")
