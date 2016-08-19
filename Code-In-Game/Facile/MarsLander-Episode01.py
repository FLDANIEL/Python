import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if v_speed <= -40:
        print('0 4')
        
    elif v_speed >= -40:
        print("0 2")
        
    else:
print('0 3')
