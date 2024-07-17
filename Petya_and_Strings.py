# string1 = input()
# string2 = input()

# new_string1 = string1.upper()
# new_string2 = string2.upper()

# size1 = 0
# size2 = 0

# for i in range(len(string1)):
#   size1 += ord(new_string1[i])
#   size2 += ord(new_string2[i])

# if size1 < size2:
#   print(-1)
# elif size1 > size2:
#   print(1)
# elif size1 == size2:
#   print(0)


"""Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

Examples
input
aaaa
aaaA
output
0
"""
string1 = input()
string2 = input()

new_string1 = string1.upper()
new_string2 = string2.upper()


if new_string1 < new_string2:
  print(-1)
elif new_string1 == new_string2:
  print(0)
else:
  print(1)