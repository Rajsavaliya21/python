# 60. Write a Python program to read a random line from a file.

import random

file_path = 'text.txt'  
with open(file_path, 'r') as file:
    lines = file.readlines()

if not lines:
    print("The file is empty.")
else:
    random_index = random.randint(0, len(lines) - 1)
    
    random_line = lines[random_index].strip()  
    print("Random Line:", random_line)
