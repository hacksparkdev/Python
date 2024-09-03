# Functions


### Defining a function

```
def greet_user():
    print("Hello")

greet_user()

```

### Passing information to a funtion

```
def greet_user(username):
    print(f"Hello {username.title()}")

greet_user("bob")

```


### Parameter VS Arguments

```
def greet_user(username <<--- Parameter):
    
    print(f"Hello {username.title()}")

greet_user('Greg' <<------ Argument)

```

- Parameter - Name listed in the function definition. 
- Argument - The Real values passed to the function.




