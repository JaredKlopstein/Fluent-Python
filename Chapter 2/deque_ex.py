from collections import deque

#create a deque with a length of 5 
dq = deque(range(5), maxlen=5)
print(dq)

#shifts the dq by 2
dq.rotate(2)
print(dq)

#shifts the dq back by 2
dq.rotate(-2)
print(dq)

#adds -1 to from, but removes 4 from end
dq.appendleft(-1)
print(dq)