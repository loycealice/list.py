my_list=[]

# Append elements 10,20.30,40
my_list.extend ([10,20,30,40])

# Insert 15 at the second position
my_list.insert(1, 15)

# Extend with list[50, 60, 70]
my_list.extend ([50, 60, 70])

# Remove the last element
my_list.pop ()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of 30
index = my_list.index(30)
print(index)