filename = 'names.txt'

with open(filename) as f:
    lines = f.readlines()


for line in lines:
    print(line)
