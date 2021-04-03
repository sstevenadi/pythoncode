import re

hand = open(r"D:\WORK\UDINUS\MOOC\Coursera\Learning Python\re\sec.txt")

lst = list()
for lines in hand:
    numlist = re.findall('[0-9]+',lines)
    if len(numlist) == 0: continue
    for i in range (0,len(numlist)):
        lst.append(int(numlist[i]))

print(sum(lst))

# import re below is not my code

# hand = open("regex_sum_24962.txt")
# x=list()
# for line in hand:
#      y = re.findall('[0-9]+',line)
#      x = x+y

# sum=0
# for z in x:
#     sum = sum + int(z)

# print(sum)

# need to learn moRE !!