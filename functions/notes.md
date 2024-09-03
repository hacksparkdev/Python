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


### Positional Arguments

```
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name}")

describe_pet()

```

- The Arguments should be given in the order the parameters are.


### Returning Dictionary

```
def build_person(first_name, last_name):
    person = {'first': first_name, 'lastname': last_name}
    return person

musician = build_person('Corey', 'Jones')
print(musician)
```


