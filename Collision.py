import math

def rect_collision(x1, y1, a1, b1, x2, y2, a2, b2, dir_type):
    col_direction = [0, 0]
    if (((x2<=x1+a1 and x2>=x1) or (x2+a2>=x1 and x2+a2<=x1+a1) or (x1 > x2 and x1+a1 < x2+a2)) and ((y2<=y1+b1 and y2>=y1) or (y2+b2>=y1 and y2+b2<=y1+b1) or (y1 > y2 and y1+b1 < y2+b2))):
        if dir_type == "pos":
            if x2<=x1+a1 and x2>=x1:
                col_direction[0] = -1
            elif x2+a2>=x1 and x2+a2<=x1+a1:
                col_direction[0] = 1
            elif (x1 > x2 and x1+a1 < x2+a2):
                if x2+a2/2 > x1+a1/2:
                    col_direction[0] = -1
                else:
                    col_direction[0] = 1

            if y2<=y1+b1 and y2>=y1:
                col_direction[1] = -1
            elif y2+b2>=y1 and y2+b2<=y1+b1:
                col_direction[1] = 1
            elif (y1 > y2 and y1+b1 < y2+b2):
                if y2+b2/2 > y1+b1/2:
                    col_direction[1] = -1
                else:
                    col_direction[1] = 1

        elif dir_type == "bool":
            return True

    if dir_type == "pos":
        return col_direction
    return False

def circle_collision(x1, y1, r1, x2, y2, r2):
    if math.sqrt((x1-x2)**2+(y1-y2)**2)-r1 < 0 or math.sqrt((x1-x2)**2+(y1-y2)**2)-r2 < 0:
        return True
    return False