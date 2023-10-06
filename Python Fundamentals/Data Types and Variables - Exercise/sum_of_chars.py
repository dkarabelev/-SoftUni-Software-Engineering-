# User Input
num_characters = int(input())
total_sum = 0

# Logic
for character in range(num_characters):
    current_character = input()
    total_sum += ord(current_character)



# Print
print(f"The sum equals: {total_sum}")
