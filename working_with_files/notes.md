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
