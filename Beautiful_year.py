"""
It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.

Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.
"""

def distinct_year(y):
  while True :
    y += 1
    y1 = str(y)
    lst = [*y1] # lst = []
                # for letter in y:
                #    lst.append(letter)
    lst_set = set(lst)
    if len(lst_set) == len(lst):
      print(y1)
      break                  

if __name__ == "__main__":
  y = int(input())
  y1 = str(y)
  distinct_year(y)