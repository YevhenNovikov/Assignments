import random

for char_code in range(65, 91):
    filename = chr(char_code) + ".txt"
    with open(filename, 'w') as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))

summary_info = ""
for char_code in range(65, 91):
    filename = chr(char_code) + ".txt"
    with open(filename, 'r') as file:
        number = file.read()
        summary_info += f"{filename}: {number}, "

summary_info = summary_info.rstrip(", ")
with open("summary.txt", 'w') as summary_file:
    summary_file.write(summary_info)
