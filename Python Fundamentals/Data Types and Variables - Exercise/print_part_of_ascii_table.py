# User Input
start_index = int(input())
final_index = int(input())

# Logic
for number in range(start_index, final_index + 1):
    print(chr(number), end = " ")
