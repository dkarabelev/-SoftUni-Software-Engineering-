from math import pow, pi
# User input

figure = input()


area = 0

# Logic
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = pi * pow(r, 2)
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2


# Print user input
print(f'{area:.3f}')
