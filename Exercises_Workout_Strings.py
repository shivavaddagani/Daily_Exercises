# Chapter 2 : Strings
Word = input("Enter a word to convert")

def pig_latin(Word):
    if Word[0] in "aeiou":
        print("{}way".format(Word))
    else:
        print("{}{}ay".format(Word[1::],Word[0]))
pig_latin(Word)