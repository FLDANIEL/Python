import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    
    if coord_x > (road): 
        print("SLOW")
        coord_x = coord_x + speed
    elif (coord_x + speed) > road:
        print("JUMP")   
    else:
        if speed < gap + 1:        
            print("SPEED")
            coord_x = coord_x + speed
        elif speed == gap + 1:
            print("WAIT")
            coord_x = coord_x + speed
        elif speed > gap + 1:
            print("SLOW")
            coord_x = coord_x + speed
        else:
            print("WAIT")
coord_x = coord_x + speed
