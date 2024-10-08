"""
Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.
"""
s = input()
l, u= 0, 0
for char in s:
    if char.isupper():
        u += 1
    else:
        l += 1
if u > l:
    print(s.upper())
elif l > u:
    print(s.lower())
else:
    print(s.lower())