""""Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round."""

n , k = map(int,input().split())
a = list(map(int,input().split()))
count = 0
kth_score =a[k-1]
for a_s in a:
  if a_s >= kth_score and a_s > 0:
    count += 1
print(count)