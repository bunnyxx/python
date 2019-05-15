replacements = ('a', '4'), ('b', '8'), ('f', 'ph'), ('g', '9'), ('e', '3'), ('o', '0'), ('s', '2'), ('t', '7'), ('z', '2')
phrase = input("Input verse: ").lower()
newPhrase = phrase
for old, new in replacements:
  newPhrase = newPhrase.replace(old, new)
print(newPhrase.upper())
