# Example 1:
names = ["Jennifer", "Alfred", "Jack"]
gpas = [4.0, 3.1, 2.7]
sort_all([names, gpas])
print(names)  # Output is ["Alfred", "Jack", "Jennifer"]
print(gpas)   # Output is [3.1, 2.7, 4.0]

# Example 2:
names = ["Jennifer", "Alfred", "Jack"]
gpas = [4.0, 3.1, 2.7]
sort_all([gpas, names]) # we are sorting by GPA this time
print(names)  # Output is ["Jack", "Alfred", "Jennifer"]
print(gpas)   # Output is [2.7, 3.1, 4.0]
