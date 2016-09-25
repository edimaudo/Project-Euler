def route_num(cube_value):
    size = [1] * cube_value
    for value in range(cube_value):
        for value2 in range(value):
            size[value2] = size[value2] + size[value2-1]
        size[value] = 2 * size[value - 1]
    return size[cube_value - 1]


print(route_num(20))