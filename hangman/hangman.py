def found_list():
    index=0
    found=0
    for letter in word_list:
        if input_letter== letter:
            found=1
            guess_list[index]= letter
        index= index+1


    return found

import random
data= open("sowpods.txt").readlines()
word = random.choice(data)
print("")
print("Welcome to Hangman! Here are a few rules. You only have 6 wrong guesses. After that, you LOSE! Also after you enter a letter make sure to hit enter. Have fun :) ")
print("")
#print(word)

word_len = len(word)-1

#print(word_len)

x= "_"*word_len
#print(x)

word = word[:-1]
word_list= list(word)
guess_list= list(x)
wrong_list= list()
print(guess_list)
print("")

turn= 1
while turn<=6:
    input_letter=raw_input("Enter a Letter: ")
    print("")
    input_letter = input_letter.lower()
    try:
        if guess_list.index(input_letter)>=0:
            print("Value Already Guessed")
            print("")
        elif wrong_list.index(input_letter)>=0:
            print("Value Already Guessed")
            print("")

            break
    except ValueError:
        if found_list()==0:
            turn = turn+1
            wrong_list.append(input_letter)
            print("Letter not Found")
            print("")
            print("Wrong Values:" + str(wrong_list))
            print("")
        print(guess_list)
        print("")
        if guess_list==word_list:
            print("You Win!")
            print("")
            exit()
print("You Lose!")
print("")
print("The word was:" + word)
