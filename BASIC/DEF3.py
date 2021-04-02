def meks(x):
    a = 0
    for b in x:
        if b > a:
            a = b
    return a

list1 = [1,2,3,4,5,6] 
list2 = [9,2,10,14,5,6] 
list3 = [11,12,4,8,3,9] 
list4 = [11,22,33,24,55,66,77,100] 

print ("="*30)

print("List 1")
print (meks(list1),"\n")

print("List 2")
print (meks(list2),"\n")

print("List 3")
print (meks(list3),"\n")

print("List 4")
print (meks(list4))

print ("="*30)



