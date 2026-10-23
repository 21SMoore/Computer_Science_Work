total_score = 0
while True:
    
    lst = []
    word = input("enter a word: ")
    word = word.upper()
    points = 0
    
    for x in word:
        lst += x

    if word.isalpha():
        for x in lst:
            if "A" in x:
                points += 1
            elif "E" in x:
                points += 1
            elif "I" in x:
                points += 1
            elif "O" in x:
                points += 1
            elif "U" in x:
                points += 1
                
            elif "V" in x:
                points += 5
            elif "W" in x:
                points += 5
            elif "X" in x:
                points += 5
            elif "Y" in x:
                points += 5
            elif "Z" in x:
                points += 5
                
            else:
                points += 3
            
            
        total_score += points
        print(f"Word:{word}, Score:{points}, Total Score:{total_score}")
        
        
        
            
            
    else:
        print("error")
        continue
    
    choice = input("play again? [Y/N] : ") #choice doesnt matter
    if choice == "y" or "Y":
        continue
    else:
        print("your total score was",total_score)
        break 