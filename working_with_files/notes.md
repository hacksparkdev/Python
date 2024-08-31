## Reading files in same path

```
filename = 'names.txt'
with open('filename') as f:
    contents  = f.read()
    print(contents)
```

- With open - Opens the file in the filename variable. 
- as f - Creates a variable for the file name f
- f.read() - Reads files contents 
- print(contents) - Prints the contents of the file


## Relative Path

```
filename = 'names.txt'
with open('text_files/filename') as f:
    contents = f.read()
    print(contents)
```

- text_files/filename - This is the path to the file that will be read


## Reading file line by line

```
filename = 'names.txt'
with open('filename') as f:
    for line in f:
        print(line)
```
The for loop reads each line from f and adds it to line each time around line has a different value. 

- for line in f: - This line asigns the contents of the variable f to the varable line
- print(line) - Prints the contents of line (wich is the contents of f)


# Creating a list from file contents

```
filename = names.txt

with open('filename') as f:
    lines = f.readlines()

for line in lines:
  print(line.rstrip())

```

  - lines = f.readline() - This line takes the data from the file and add it to a list that you can work with outside of the (with open) block.


### Writing Files

```
filename = 'programming.txt'
with open(filename, 'w') as f:
    f.write('I love Programming')
```





