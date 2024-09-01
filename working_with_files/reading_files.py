

try:
    with open("textfiles/antichrist.txt", encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    msg = f'Sorry, the file ${filename} does not exist'
    print(msg)

else:
    words = contents.split()
    num_words = len(words)
    print(f'The file has {num_words} words.')
