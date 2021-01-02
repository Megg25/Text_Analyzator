TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

oddelovac = "=" * 60
print(oddelovac)
print("Welcome to the app. Please log in")
USERNAME = input("Username: ")
PASSWORD = input("Your password: ")
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

if USERNAME == "bob" and PASSWORD == "123":
    print("Username and password is OK, continue")
elif USERNAME == "ann" and PASSWORD == "pass123":
    print("Username and password is OK, continue")
elif USERNAME == "mike" and PASSWORD == "password123":
    print("Username and password is OK, continue")
elif USERNAME == "liz" and PASSWORD == "pass123":
    print("Username and password is OK, continue")
else:
    print("Sorry your username and password is wrong")
    exit()

print(oddelovac)

print("Now, we have 3 texts to be analyzed.Choose one of them.")
text_number = input("Enter a number btw. 1 and 3 to select: ")
for a in text_number:
    if a.isalpha() or a == "." or a == ",":
        print("Sorry,", text_number, "is incorrect")
        exit()

print(oddelovac)
if int(text_number) == 1:
    your_text = TEXTS[0]
    print(your_text)
elif int(text_number) == 2:
    your_text = TEXTS[1]
    print(your_text)
elif int(text_number) == 3:
    your_text = TEXTS[2]
    print(your_text)

print(oddelovac)

words_number = your_text.split()
print("There are", len(words_number), "words in the selected text.")
words_list = your_text.split()

titlecase_words = []
[titlecase_words.append(word) for word in words_list if word.istitle()]
print("There are", len(titlecase_words), "titlecase words.")

uppercase_words = []
[uppercase_words.append(word) for word in titlecase_words if word.isupper()]
print("There are", len(uppercase_words), "uppercase words.")

lowercase_words = []
[lowercase_words.append(word) for word in words_list if word.islower()]
print("There are", len(lowercase_words), "lowercase words")

numeric_strings = []
[numeric_strings.append(numb) for numb in words_list if numb.isnumeric()]
print("There are", len(numeric_strings), "numeric strings.")

print(oddelovac)

clear_words = [word.strip(".,! ").lower() for word in words_list]
dictionary = {}
for word in clear_words:
    delka = len(word)
    if delka in dictionary.keys():
        dictionary[delka] = dictionary[delka] + 1
    else:
        dictionary[delka] = 1
keys = list(dictionary.keys())
keys.sort()
for delka in keys:
    print(delka, "|", "*" * dictionary[delka], "|", dictionary[delka])

print(oddelovac)

numeric_count = []
for numb in numeric_strings:
    numeric_count.append(int(numb))

print("If we summed all the numbers in this text we would get:", sum(numeric_count))

print(oddelovac)