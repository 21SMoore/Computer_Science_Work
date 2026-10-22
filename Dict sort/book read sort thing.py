book = open("book.txt","r")
readbook = book.read()

readbook = readbook.lower()
readbook = readbook.split()

dictionary = {}

for x in readbook:
    if x in dictionary: #increases the value of the word by 1
        dictionary[x] += 1
    else:
       dictionary[x] =  1 #this sets the value to 1 if the word is absent
       
def sorting(x):
    return x[1]
sorted_dict = sorted(dictionary.items(),key = sorting, reverse = True)[:10]
print(dict(sorted_dict))

book.close()

