# User Input
from math import ceil
num_people = int(input())
capacity = int(input())

courses = ceil(num_people / capacity)

# Print
print(courses)


