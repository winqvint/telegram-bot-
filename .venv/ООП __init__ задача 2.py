class AreaPoint:
    def __init__(self,i,j,height = 15):
        self.i = i
        self.j = j
        self.height = height
area_list = []
for j in range(3):
    row = []
    for i in range(3):
        point = AreaPoint(i,j)
        row.append(point)
    area_list.append(row)
