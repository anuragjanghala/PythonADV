strings= ['a','b','c','d']

# 8*4 = 32 bytes of storage

print(strings[2]) # O(1) - access

strings.append('e')  # O(1)/O(n) - adding to the end (can change depending upon the memory allocation)
print(strings)

strings.pop() # O(1) - deleting from end
print(strings) 

strings.insert(0, 'x') # O(n) - adding value to specific index (shifting)
print(strings)

strings.remove('d') # O(n) - removing specific value after linear scan
print(strings)