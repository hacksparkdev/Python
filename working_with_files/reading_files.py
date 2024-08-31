filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write('I love programming')

with open(filename) as f:
    contents = f.read()
    print(contents)
    
