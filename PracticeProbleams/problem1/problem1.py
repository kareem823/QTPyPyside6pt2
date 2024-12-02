#sorting strings
arr = ["apple", "banana", "cherry", "date", "elderberry"]

arr.sort()
print(arr)

#sort by length of the string
arr.sort(key=lambda x: len(x))
print(arr)