filename = 'antichrist.py'

with open(f'textfiles/antichrist.txt', encoding='utf-8') as f:
    contents = f.read()


words = contents.split()
print(len(words))
