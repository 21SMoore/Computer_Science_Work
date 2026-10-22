sentence = input("Enter a sentence: ")
choice = input("Sort by word or letter?: ")
choice = choice.lower()
sentence_new = []
if choice == "word":
    sentence_new = sentence.split()
else:
    for x in sentence:
        if x == " ":
            continue
        else:
            sentence_new += x

dictionary = {}

for x in sentence_new:
    if x in dictionary: #increases the value of the word by 1
        dictionary[x] += 1
    else:
       #dictionary.update({x:1})

       dictionary[x] =  1 #this sets the value to 1 if the word is absent


print(dictionary)