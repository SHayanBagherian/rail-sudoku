import numpy as np
import matplotlib.pyplot as plt

n = 4


def random_on_border():
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


#ingr = initial_grid
ingr = np.full((n, n), ".", dtype="<U4")
start = list(random_on_border())
end = list(random_on_border())
# Ensure start and end points do not overlap
while start[:2] == end[:2]:
    end = list(random_on_border())

print(f"Start: {start}")
print(f"End:   {end}")

def neighbor_with_end(x,y,i):
    if abs(abs(int(end[0]) - x) + abs(int(end[1])- y)) == 1 and i>(n-1):
        return True
    return False

def nc(point_x,point_y, list_grid,i): #neighbor check
    neighbors = ""
    if neighbor_with_end(point_x,point_y,i):
        if point_x - 1 == int(end[0]):
            return "u" ,True
        if point_x+1 == int(end[0]):
            return "d",True
        if point_y - 1 == int(end[1]):
            return "l",True
        if point_y + 1 == int(end[1]):
            return "r",True

    if point_x - 1 >= 0:
        if list_grid[point_x - 1, point_y] == '.':
            neighbors +="u"
    if point_x + 1 <= n-1 :
        if list_grid[point_x + 1, point_y] == '.':
            neighbors +="d"
    if point_y - 1 >= 0 :
        if list_grid[point_x, point_y -1] == '.':
            neighbors +="l"
    if point_y + 1 <= n-1:
        if list_grid[point_x, point_y +1] == '.':
            neighbors +="r"
    return neighbors,False

def rns(point_x, point_y, grid,i):
    neighbors , final = nc(point_x, point_y, grid,i)
    if not neighbors:
        return "b", point_x, point_y , final
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
    return chosen_dir, new_x, new_y , final

def first_dir(x,y,dir):
    if dir == "u":
        dir = "d"
    elif dir == "d":
        dir = "u"
    elif dir == "l":
        dir = "r"
    elif dir == "r":
        dir = "l"
    if [x, y] != [int(end[0]), int(end[1])]:
        ingr[x, y] = dir
    return ingr

def move(cxindex, cyindex ,ingr,pathway,i):
    direction, next_x, next_y ,final= rns(cxindex, cyindex, ingr,i)
    if direction == "b":
        ingr[cxindex, cyindex] = "-"
        pathway.pop()
        cxindex, cyindex = pathway[-1][0],pathway[-1][1]
        ingr[cxindex, cyindex] = str(ingr[cxindex, cyindex])[:-1]
        return cxindex, cyindex, ingr, final

    ingr[cxindex, cyindex] += direction
    ingr = first_dir(next_x, next_y,direction)
    pathway.append([next_x, next_y])
    return next_x, next_y, ingr, final

def path_builder(ingr):
    i=0
    pathway = [start[:2]]
    xindex , yindex = start[0],start[1]
    ingr[start[0],start[1]] = start[2]
    ingr[end[0],end[1]]= end[2]
    final = False
    while final == False:
        xindex, yindex, ingr,final = move(xindex, yindex ,ingr,pathway,i)
        i+=1
        print(ingr)
        print("---")
    final_direction = str(ingr[pathway[-2][0],pathway[-2][1]])[-1]
    if  final_direction == "u":
        ingr[end[0],end[1]] += 'd'
    if  final_direction == "d":
        ingr[end[0],end[1]] += 'u'
    if  final_direction == "l":
        ingr[end[0],end[1]] += 'l'
    if  final_direction == "r":
        ingr[end[0],end[1]] += 'l'

    return ingr,pathway
ingr,pathway = path_builder(ingr)