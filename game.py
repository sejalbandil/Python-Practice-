while True:
    one = raw_input("Player One-Rock, Paper or Scissors:")
    two = raw_input("Player Two-Rock, Paper or Scissors:")
    one= one.lower()
    two= two.lower()
    if one == two:
        print("tie")
    elif one== "rock" and two=="paper":
        print("Player Two Wins!")
    elif one=="rock" and two=="scissors":
        print("Player One Wins!")
    elif one=="paper" and two=="rock":
        print("Player One Wins!")
    elif one=="paper" and two=="scissors":
        print("Player Two Wins!")
    elif one=="scissors" and two=="rock":
        pring("Player Two Wins!")
    elif one=="scissors" and two=="paper":
        print("Player One Wins!")
    ask= raw_input("Do You Want To Play Again?")
    ask=ask.lower()
    if ask=="yes":
        continue
    if ask=="no":
        break
