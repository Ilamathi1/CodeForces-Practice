n = int(input())
current_size = 0
minimum_needed = 0
for i in range(n):
  a, b = map(int,input().split())
  current_size -= a
  current_size += b
  if minimum_needed < current_size:
    minimum_needed = current_size

print(minimum_needed)