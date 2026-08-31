import numpy as np
import matplotlib.pyplot as plt

n = 4


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

def rns(point_x,ponit_y,list):
    neighbor = nc(point_x,ponit_y,list)
    selector = np.random.randint(0,len(neighbor))
    return str(neighbor[selector])
#ingr = initial_grid
ingr = np.full((n,n),".", dtype="<U2")

start = np.random.randint(0,n,1)
ingr[0,start]= "u" + rns(0,start,ingr)


print(start)
print(ingr)