import json

with open('input.json', 'r') as file:
    data = json.load(file)

with open('input.txt', 'w') as file:
    file.write(str(data))
