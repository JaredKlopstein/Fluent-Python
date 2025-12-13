fruits = ['grape', 'raspberry', 'apple', 'banana']
#produces a new list that is sorted
print(sorted(fruits))
print(fruits)

#produces a new list that is sorted in reverse
print(sorted(fruits,reverse=True))

#produces a new list that is sorted by length
print(sorted(fruits, key=len))

#produces a new list that is sorted by length in reverse
print(sorted(fruits, key=len, reverse=True))

#using id to show that the list is changed
print(f" sorted id: {id(sorted(fruits))}")
fruits.sort()
print(f" sort id: {id(fruits)}")

