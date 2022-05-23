
def map_vertices(wirepath):
    position = [0,0]
    vertices = []
    for move in wirepath:
        direction = move[0]
        distance = int(move[1:])
        if direction == 'R':
            position[0] += distance
        elif direction == 'U':
            position[1] += distance
        elif direction == 'L':
            position[0] -= distance
        elif direction == 'D':
            position[1] -= distance
        
        vertices.append(position.copy())
    
    return vertices

"""
Simple method I wrote when I planned on doing this calculation more than once. not so necessary now.
"""
def manhattan_distance(x, y):
    return abs(x) + abs(y)

"""
If the deltas of either their x or their y are equal then
they must be parallel
"""
def is_parallel(p11, p12, p21, p22):
    dy1 = p12[1] - p11[1]
    dy2 = p22[1] - p21[1]
    dx1 = p12[0] - p11[0]
    dx2 = p22[0] - p21[0]
    return dx1 == dx2 or dy1 == dy2


def get_steps_from_segment(p1, p2):
    if p1[0] == p2[0]:
        return abs(p2[1] - p1[1])
    else:
        return abs(p2[0] - p1[0])


def get_wire_steps(wirepath, end_position, intersection):
    steps = 0
    for i in range(0, end_position):
        if i == end_position - 1:
            steps += get_steps_from_segment(wirepath[i], intersection)
        else:
            steps += get_steps_from_segment(wirepath[i], wirepath[i+1])

    return steps

"""
The basic premise is that all lines are perpendicular or parallel in this problem because of the movement
If they are parallel they cannot intersect ever
If they are perpendicular there is a point that their theoretical infinite line would intersect, but that point
has to lie within the bounds of their min and max x,y values so I use the topmost y and bottom most y from the 
vertical line and the leftmost and rightmost x from the horizontal line and then test the theoretical intersection point
against it.
"""
def get_intersection(p11, p12, p21, p22):
    if is_parallel(p11, p12, p21, p22):
        return [0,0]
    # Then they're perpendicular
    intersect_x = 0
    intersect_y = 0
    topmost_y = bottommost_y = 0
    leftmost_x = rightmost_x = 0

    # Find theoretical intersection point and test points
    if p11[0] == p12[0]:
        # line segment 1 is vertical so line segment 2 is horizontal
        intersect_x = p11[0]
        intersect_y = p21[1]
        topmost_y = p11[1] if p11[1] > p12[1] else p12[1]
        bottommost_y = p11[1] if p11[1] < p12[1] else p12[1]
        leftmost_x = p21[0] if p21[0] < p22[0] else p22[0]
        rightmost_x = p21[0] if p21[0] > p22[0] else p22[0]
    elif p21[0] == p22[0]:
        # line segment 2 is vertical so line segment 1 is horizontal
        intersect_x = p21[0]
        intersect_y = p11[1]
        topmost_y = p21[1] if p21[1] > p22[1] else p22[1]
        bottommost_y = p21[1] if p21[1] < p22[1] else p22[1]
        leftmost_x = p11[0] if p11[0] < p12[0] else p12[0]
        rightmost_x = p11[0] if p11[0] > p12[0] else p12[0]
    else:
        print("This shouldn't have happened by my logic")

    if intersect_x < rightmost_x and intersect_x > leftmost_x and intersect_y < topmost_y and intersect_y > bottommost_y:
        return [intersect_x, intersect_y]
    else:
        return [0, 0]

"""
Start of the main program. at this stage I may change to the if __main__ check to better delineate
"""
wirepaths = {}
with open("2019/inputs/3.txt", 'r') as f:
    input = f.read()
    wirepaths = input.splitlines()
    for i, wirepath in enumerate(wirepaths):
        wirepaths[i] = wirepath.split(",")

w1_vertices = map_vertices(wirepaths[0])
w2_vertices = map_vertices(wirepaths[1])

w1_vertices.insert(0, [0,0])
w2_vertices.insert(0, [0,0])

least_total_steps = 0
for i in range( 0, len(w1_vertices) - 1):
    for j in range(0, len(w2_vertices) - 1):
        intersection = get_intersection(w1_vertices[i], w1_vertices[i + 1], w2_vertices[j], w2_vertices[j + 1])
        if intersection[0] != 0 or intersection[1] != 0:
            steps_1 = get_wire_steps(w1_vertices, i+1, intersection)
            steps_2 = get_wire_steps(w2_vertices, j+1, intersection)
            
            if least_total_steps == 0 or steps_1 + steps_2 < least_total_steps:
                least_total_steps = steps_1 + steps_2


print(least_total_steps)
