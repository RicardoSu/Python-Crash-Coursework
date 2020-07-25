alice = 'cats.txt'

f = open("cats.txt", "r")
text = f.read()
print(text.lower().count('leo'))
