import numpy as np
import matplotlib.pyplot as plt

n = 4


def random_on_border(ingr):
    yindex = np.random.randint(0, n)
    xindex = np.random.randint(0,4)
    if xindex == 0:
        return 0 , yindex , 'u'
    elif xindex==1:
        return yindex,0 , 'l'
    elif xindex==2:
        return n-1,yindex ,'d'
    else:
        return yindex,n-1 , 'r'
    
def nc(point_x,point_y, list): #neighbor check
    neighbors = ""
    if point_x - 1 >= 0:
        if list[point_x - 1, point_y] == '.':
            neighbors +="u"
    if point_x + 1 <= n-1 :
        if list[point_x + 1, point_y] == '.':
            neighbors +="d"
    if point_y - 1 >= 0 :
        if list[point_x, point_y -1] == '.':
            neighbors +="l"
    if point_y + 1 <= n-1:
        if list[point_x, point_y +1] == '.':
            neighbors +="r"
    return neighbors

def rns(point_x, point_y, grid):
    neighbors = nc(point_x, point_y, grid)
    if not neighbors:
        return "", point_x, point_y
    selector = np.random.randint(0, len(neighbors))
    chosen_dir = neighbors[selector]
    new_x, new_y = point_x, point_y
    if chosen_dir == "u":
        new_x -= 1
    elif chosen_dir == "d":
        new_x += 1
    elif chosen_dir == "l":
        new_y -= 1
    elif chosen_dir == "r":
        new_y += 1
    return chosen_dir, new_x, new_y

def first_dir(x,y,dir):
    if dir == "u":
        dir = "d"
    elif dir == "d":
        dir = "u"
    elif dir == "l":
        dir = "r"
    elif dir == "r":
        dir = "l"
    ingr[x, y] = dir
    return ingr
def move(cxindex, cyindex ,ingr):
    direction, next_x, next_y = rns(cxindex, cyindex, ingr)
    ingr[cxindex, cyindex] += direction
    ingr = first_dir(next_x, next_y,direction)
    return next_x, next_y, ingr

#ingr = initial_grid
ingr = np.full((n, n), ".", dtype="<U2")

xindex, yindex, starting_direction = random_on_border(ingr)
print(xindex,yindex)
pathway = [[xindex,yindex]]
ingr[xindex, yindex] = starting_direction
xindex, yindex, ingr = move(xindex, yindex ,ingr)
pathway.append([xindex,yindex])
xindex, yindex, ingr = move(xindex, yindex ,ingr)
pathway.append([xindex,yindex])
xindex, yindex, ingr = move(xindex, yindex ,ingr)
pathway.append([xindex,yindex])
print(ingr)