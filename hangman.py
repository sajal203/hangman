import random
lst= ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust',
      'dent','market','knock','smite','windy','coin','throw','silence','bluff','downfall',
      'climb','lying','weaver','snob','kickoff',]



def play():
    wr = random.choice(lst)
    guesses = " "
    turns = 6
    print(display_hangman(turns))
    while turns > 0:
        failed = 0
        for char in wr:
            if char in guesses:
                print(char)
            else:
                print("_",end = " ")
                failed += 1
        if failed == 0:
            print("you win")
            break
        print("")
        guess = input("enter the character: ")
        guesses += guess
        if guess not in wr:
            turns -= 1
            print(display_hangman(turns))
            if turns == 0:
                print("you lose")
                print("the word was: ", wr)







def display_hangman(turns):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[turns]

def main():
    play()
    while input("do you want to continue y/n: ").upper() == 'Y':
        play()

if __name__ == '__main__':
    main()
