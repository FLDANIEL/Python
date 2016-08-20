import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
conv = []
for c in message:
    conv.append('{0:07b}'.format(ord(c)))
binary = ''.join(conv) + "S"

p = 0
answer = ""
for l in binary:
     
    nextc = p
       
    if binary[p] == "1":
        answer = answer + "0" + " "
        while True:
            nextc = nextc + 1           
            if binary[nextc] == "1":
                answer = answer + "0"
            elif binary[nextc] == "0":
                answer = answer + "0" + " "
                break
            else:
                answer = answer + "0"
                break
                              
    elif binary[p] == "0":
        answer = answer + "00" + " "
        while True:
            nextc = nextc + 1
            if binary[nextc] == "0":
                answer = answer + "0"
            elif binary[nextc] == "1":
                answer = answer + "0" + " "
                break
            else:
                answer = answer + "0"
                break
    elif binary[p] == "C":
        nextc = nextc + 1
            
    p = nextc

        
print(answer)
