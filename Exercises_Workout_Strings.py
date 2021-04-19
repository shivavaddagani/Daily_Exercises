                                     # Chapter 2 : Strings
# ======================= Problem 1 ==================
Word = input("Enter a word to convert")

def pig_latin(Word):
    if Word[0] in "aeiou":
        return("{}way".format(Word))
    else:
        return("{}{}ay".format(Word[1::],Word[0]))
print(pig_latin(Word))

# ======================= Problem 2 ===================
sentence = input("enter a sentence")
list_sentence = sentence.split(" ")            # splitting sentence into words by space delimiter

pig_latin_list = [pig_latin(i) for i in list_sentence]
new_sentence = ' '.join(pig_latin_list)
print(pig_latin_list)
print(new_sentence)

# ======================== Problem 3 ==================
# 2.4 UBBI DUBBI

word = input("enter a word")
list_word = list(word)
print(list_word)

j=0
ubbi =[]
for i in list_word:
    j += 1
    if i in "aeiou":
       ubbi.append("ub{}".format(i))
    else:
        ubbi.append(i)

ubbi_dubbi = "".join(ubbi)
print(ubbi_dubbi)



