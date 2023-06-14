while True:
    lines = input("How many lines will there be?: ")
    if not lines.isnumeric():
        print("Please enter a number")
    else: 
        break
poem = []
num_of_lines = int(lines)
for i in range(num_of_lines):
    line = input("Enter another line: ")
    poem.append(line.lower())

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"

vowels_count = []
consonants_count = []
total_vowels = 0
total_consonants = 0

for line in poem:
    current_line_vowels = 0
    current_line_consonants = 0
    for letter in line:
        if letter in vowels:
            current_line_vowels += 1
            total_vowels += 1
        elif letter in consonants:
            current_line_consonants += 1
            total_consonants += 1
    vowels_count.append(current_line_vowels)
    consonants_count.append(current_line_consonants)

print("line\tvowels\tconsonants")
for i in range(num_of_lines):
    print(str(i+1) + "\t" + str(vowels_count[i]) + "\t" + str(consonants_count[i]))
print("total\t" + str(total_vowels) + "\t" + str(total_consonants))