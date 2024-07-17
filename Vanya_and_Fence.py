n, h = map(int,input().split())
width = 0
a = list(map(int,input().split()))
for i in range(n):
  if a[i] > h:
    width += 2
  else:
    width += 1
print(width)