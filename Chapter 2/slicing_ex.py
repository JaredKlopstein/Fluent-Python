#shows how slicing prevents overlapping
l = [10,20,30,40,50,60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])

print(l[len(l):])
print(l[:len(l)])

#split using length
print(l[:(len(l)//2)])
print(l[(len(l)//2):])