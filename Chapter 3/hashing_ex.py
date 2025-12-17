#example of a touple in tuple
tt = (1, 2, (30, 40))
print(hash(tt))

#example of frozenset in tuple
tf = 1, 2, frozenset([30, 40])
print(hash(tf))

#example of list inside of tuple
tl = (1, 2, [30, 40])
print(hash(tl))

