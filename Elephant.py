"""
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.
"""
x= int(input())
remaining = x % 5
if remaining % 5 != 0:
    remaining = 1
count =  x//5 + remaining
print(count)