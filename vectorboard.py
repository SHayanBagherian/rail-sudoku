import numpy as np
import matplotlib.pyplot as plt
import math

n = 7

#Choosing a random component on the borders
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

#Building the first grid
initial_grid = np.full((n, n), ".", dtype="<U4")

#Start and end building
start = list(random_on_border())
end = list(random_on_border())
while start[:2] == end[:2]: # Ensure start and end points do not overlap
    end = list(random_on_border())

print(f"Start: {start}")
print(f"End:   {end}")

#Finding if we are neighbor with the ending point
def neighbor_with_end(x,y,i):
    if abs(abs(int(end[0]) - x) + abs(int(end[1])- y)) == 1 and i>(n-1): #i>(n-1) stop the code frome building easy problems
        return True
    return False

#Building aneighbor list
def neighbor_check(point_x,point_y, list_grid,i):
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

#Selecting a random neighbor
def random_neighbor_selector(point_x, point_y, grid,i):
    neighbors , final = neighbor_check(point_x, point_y, grid,i)
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

#finding out the first direction of the next component
def first_direction(x,y,dir):
    if dir == "u":
        dir = "d"
    elif dir == "d":
        dir = "u"
    elif dir == "l":
        dir = "r"
    elif dir == "r":
        dir = "l"
    if [x, y] != [int(end[0]), int(end[1])]:
        initial_grid[x, y] = dir
    return initial_grid

#Moving on the board
def move(cxindex, cyindex ,initial_grid,pathway,i):
    direction, next_x, next_y ,final= random_neighbor_selector(cxindex, cyindex, initial_grid,i)
    if direction == "b":
        initial_grid[cxindex, cyindex] = "-"
        pathway.pop()
        cxindex, cyindex = pathway[-1][0],pathway[-1][1]
        initial_grid[cxindex, cyindex] = str(initial_grid[cxindex, cyindex])[:-1]
        return cxindex, cyindex, initial_grid, final

    initial_grid[cxindex, cyindex] += direction
    initial_grid = first_direction(next_x, next_y,direction)
    pathway.append([next_x, next_y])
    return next_x, next_y, initial_grid, final


def path_builder(initial_grid):
    i=0
    pathway = [start[:2]]
    xindex , yindex = start[0],start[1]
    initial_grid[start[0],start[1]] = start[2]
    initial_grid[end[0],end[1]]= end[2]
    final = False
    while final == False:
        xindex, yindex, initial_grid,final = move(xindex, yindex ,initial_grid,pathway,i)
        i+=1
    final_direction = str(initial_grid[pathway[-2][0],pathway[-2][1]])[-1]
    if  final_direction == "u":
        initial_grid[end[0],end[1]] += 'd'
    if  final_direction == "d":
        initial_grid[end[0],end[1]] += 'u'
    if  final_direction == "l":
        initial_grid[end[0],end[1]] += 'r'
    if  final_direction == "r":
        initial_grid[end[0],end[1]] += 'l'

    return initial_grid,pathway
initial_grid,pathway = path_builder(initial_grid)
print(initial_grid,"\n",pathway)

#Showing the player
gg= np.full((n, n), ".", dtype="<U4")
gg[start[0],start[1]]= initial_grid[start[0],start[1]]
gg[end[0],end[1]]= initial_grid[end[0],end[1]]
shown = [[start[0],start[1]],[end[0],end[1]]]
for i in range(math.floor(math.sqrt(len(pathway)))-2):
    selected_box = pathway[np.random.randint(1,n-1)]
    while selected_box in shown:
        selected_box = pathway[np.random.randint(1,n-1)]
    gg[selected_box[0],selected_box[1]]=initial_grid[selected_box[0],selected_box[1]]

condition = (initial_grid != '.') & (initial_grid != '-')
row_counts = np.sum(condition, axis=1)
col_counts = np.sum(condition, axis=0)
print(row_counts)
print(col_counts)
print(gg)