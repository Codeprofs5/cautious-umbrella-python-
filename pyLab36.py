# Write a program a string and print each individual
# word of it along with its length.
word = input("Describe yourself in a few words\n")
word = word.split()
for i in word:
    print(f"{i} -> word length : {len(word)}")
