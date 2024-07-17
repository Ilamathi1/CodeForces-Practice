"""
Anton likes to play chess, and so does his friend Danik.

Once they have played n games in a row. For each game it's known who was the winner — Anton or Danik. None of the games ended with a tie.

Now Anton wonders, who won more games, he or Danik? Help him determine this.
"""
n = int(input())
s = input()
a_s = 0
d_s = 0
for char in s:
    if char == 'A':
        a_s +=1
    else:
        d_s +=1
if a_s > d_s:
    print("Anton")
elif a_s < d_s:
    print("Danik")
else:
    print("Friendship")
   