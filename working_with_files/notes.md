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


## Creating a list from file contents

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

- with open(filename, 'w') as f - This line Opens the file in "Write mode"
- f.write('I love programming') - Here we write the string 'I love programming' to the file 'programming.txt'.

## Appending to files

```
filename = 'programming.txt'

with open(filename, 'a') as f:
    f.write('This is appended text.')
```

- with open(filename, 'a') as f: - This line opens the file in append mode.
- This will add to the end of a existing file instead of writing over a file.


## Analyzing text

```
filename = 'antichrist.py'

with open(f'textfiles/antichrist.txt', encoding='utf-8') as f:
    contents = f.read()


words = contents.split()
print(len(words))

```

- contents.split() - The split method spearates a string into parts wherever it finds a space and stores all the parts of a string into a list.
- print(len(words)) - This prints the length of the list.
- You can use this to count the number of words in a txt file. 


# Json


## Using json.dump() and json.load()


### json.dump()

```
import json
numbers = [2,65,684,364,6548,6,5,8,3]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
```

 - Here we create a list of numbers, create a variable with 'filename' this will be the name of the file that the list is saved into
 - json.dump(numbers, f) - This uses json.dump() to store the list


### json.load()
```
import json

filename = 'numbers.json'

with open(filename) as f:
    number = json.load(f)

print(numbers)
```


## Saving and Reading User-Generated Data


### Saving
```
import json

username = input('What is your name? ')

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back {username}")

```

- This code take user input, then dumps it into a json file


### Reading

```
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}")
```














