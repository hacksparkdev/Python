def build_person(first_name, last_name):
    person = {'first': first_name, 'lastname': last_name}
    return person

musician = build_person('Corey', 'Jones')
print(musician)
