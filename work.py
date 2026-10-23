# Function to calculate readability score of text 
def calculate_readability_score(text):
 
    # Split the text into a list of words 
    words = text.split() 
    print("The list of words in the text is:\n", words)
 
   # Initialise the word counters 
    word_count = len(words) # Number of words in list
    
    # short word count
    short_word_count = 0
    for x in words:
        if len(x) == 1:
            short_word_count += 1
        else:
            continue
    print("Short Words: ",short_word_count)
    
    # vii) complex words:
    vowel_count = 0
    complex_words = 0
    
    for x in words:
        if "a" in x:
            vowel_count += 1
        elif "e" in x:
            vowel_count += 1
        elif "i" in x:
            vowel_count += 1
        elif "o" in x:
            vowel_count += 1
        elif "u" in x:
            vowel_count += 1
            
        elif vowel_count >= 3:
            complex_words += 1
    
    print("Complex words: ",complex_words)
            
    
    # Initialise the number of sentences 
    sentence_count = text.count(".")
    sentence_count += text.count("!") # new
    
    '''
    # Calculate the readability score 
    score = word_count * sentence_count 
    score = round(score, 2) # Round the score to 2 d.p. 
    return score
    '''
    # vi) ----> its like 5 off and idk why
    left = word_count / sentence_count
    top = word_count - short_word_count
    right = top / word_count
    
    multiply = 100 * right
    bracket = left + multiply
    score = bracket * 0.4
    
    return score
    
# Set the text for analysis 
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways." 
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1 
score1 = calculate_readability_score(text1)

# printing the scores
print("The readability score 1:",score1,"\n")

# calculate the score for text 2
score2 = calculate_readability_score(text2) # new

print("The readability score 2:",score2,"\n")

# finding which text is easier to read
if score1 == score2:
    print("Both texts have the same rating")
elif score1 < score2:
    print("The first text is easier to read")
elif score1 > score2:
    print("The second text is easier to read")