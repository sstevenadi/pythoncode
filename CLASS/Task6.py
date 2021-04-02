from collections import deque

stack1 = deque()
stack2 = deque()

for a in range(10):
    b = int(input("Input Number : "))
    if b % 2 == 0 :
        stack2.append(b)
    else:
        stack1.append(b)

print ("Stack 1 isinya",stack1)
print ("Stack 2 isinya",stack2)