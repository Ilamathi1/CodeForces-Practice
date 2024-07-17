"""
There are n stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.
"""
n = int(input())
s = input()
count =0 
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
print(count)