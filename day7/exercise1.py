# This program is for getting a dictionary values cubes of keys, i.e
# {1: 1, 2: 8, 3: 27}

def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube

print(cube_finder(10))
