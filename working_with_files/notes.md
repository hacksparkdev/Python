## Reading files in same path

```
filename = 'names.txt'
with open('filename') as f:
    contents  = f.read()
    print(contents)
```

## Relative Path

```
filename = 'names.txt'
with open('text_files/filename') as f:
    contents = f.read()
    print(contents)
     

```
