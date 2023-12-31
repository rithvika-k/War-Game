# Rithvika Kathroju
# Mrs.Mansi - ICS 2O1 - 12/9/2020
# Unit 3: Programming Structures in Python - Final "War Assignment"

"""
NOTE: These are the additional things/features I added to my program:
1. Used a function 
2. Created counters for total number of rounds played, rounds won by player 1, rounds won by player 2, and rounds tied
3. Presented in a organized and neat way with graphics 
4. Incorporated a 'Prize' feature which gives the winner of the game a prize 
5. Incorporated a "Fun Questionnaire" feature so that it is more interactive 
6. Asked the user if they want to play again - used loops
7. Allowed user to have the option to play against a friend or Rosie The Robot
8. Included a Game Summary 
9. User gives a rating for the card game
"""

# In order to generate random numbers for the players we have to import the random class. 
# This will allow us to use the randint function. I will also be using the choice function. 
import random 

# I defined a function that contains the main functionality of the war card game. 
# By creating a function to do this, it will help make my code easier to understand and more visually appealing 
def war_card_game():
    
    # First, I intialize variables that store the score/number of points each player starts with 
    # This score will increase or decrease based on whether or not they win a round. 
    # Deals out 26 points to each player because 52/2 = 26
    player_1_points = 26
    player_2_points = 26
    
    """
    Intializing variables as counters by setting them equal to zero.  
    The counters keep track of the number of total rounds, rounds won by player 1, rounds won by player 2, and rounds that were a tie
    A series of conditions are checked after each round(if player 1 wins, player 2 wins, or tie) and based on the condition that equals 
    true the program will increment the responding counter by 1. 
    """
    total_rounds = 0
    p1_rounds = 0
    p2_rounds = 0
    tie_rounds = 0
    
    
    # Starting Number of Points Per Player
    # Subheading
    print("==============================================================================================")
    print("♠ ♣ ♥ ♦                                𝐏𝐎𝐈𝐍𝐓𝐒                                         ♠ ♣ ♥ ♦")
    print("==============================================================================================")
    print("Players! Here are your starting points!")
    # Lets the players know the number of points they each start the game with. 
    # I concatenated the strings/variables together because I did not want to use commas. If I used commas, spaces will be automatically inserted.
    print(player_1 + " has " + str(player_1_points) + " points.")
    print(player_2 + " has " + str(player_2_points) + " points.")
    
    # Subheading
    print("==============================================================================================")
    print("♠ ♣ ♥ ♦                                  𝐏𝐋𝐀𝐘                                          ♠ ♣ ♥ ♦")
    print("==============================================================================================")
    print("Ready? Set! Go! Let The War Begin!")
    print("----------------------------------------------------------------------------------------------")
        
    # While Loop Inside war_card_game() Function Starts Executing
    # This loop consists of the main game where players are able to see the data for each round, as well as the winner for the entire game. 
    """
    #Functionality 
    
    First, the while loop will always execute indefinitely as i set the expression to evalaute to True. More specific conditions will be checked later in the loop. 
    After that, the interpretor will go through each if-elif-else statment and then execute the one that results to True. If player 1 scores a maximum total of 52 points  
    and likewise player 2 is left with 0 points, then player 1 will be decleared the winner of the game and break out of the loop. Else if player 2 scores a maximum total 
    of 52 points and likewise player 1 is left with 0 points, then player 2 will be decleared the winner of the game and break out of the loop. If both of those conditions 
    are not met it will move onto the Else branch which will continue the game by generating numbers and keeping score of points until a player reaches the maximum 
    number of points and is decleared a winner. 
    """
    while True:
        """
        The if conditional statement checks to see if player 1 has scored a total of 52 points and likewise if player 2 has scored 0 points. If those conditions result in 
        a boolean expression that equals to True then player 1 will be declared as the winner of the entire game, and player 2 will be informed that they lost the game. As 
        an additional, I added a prize feature which randomly selects a prize from the prize list for player 1, the winner. Another feature is added which allows the user
        to answer a fun questionaire! A game summary will also be printed. After this is executed the loop will break. 
        """
        if player_1_points == 52 and player_2_points == 0:
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                                 𝐑𝐄𝐒𝐔𝐋𝐓𝐒                                       ♠ ♣ ♥ ♦")
            print("==============================================================================================")            
            # Prints out the winner and loser of the game using concatenation and typecasting.
            print("Congratulations, " + player_1 + "! You Won the Game With 52 Points!")
            print("Sorry, " + player_2 + "! You Lost the Game! Better Luck Next Time!")
            
            
            # Prize feature which allows player 1, the winner in this condition, to win a random prize. 
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                                  𝐏𝐑𝐈𝐙𝐄𝐒                                        ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            # Intializing a variable that stores a list of 4 different possible prizes the winner can win
            prizes_winner = ['$10 Tim Horton\'s Gift Card', 'Apple Watch SE', '$20 iTunes Gift Card', '$30 Amazon Gift Card']
            
            
            # Intializing a variable that stores the prize selected by the choice function. 
            # The choice method in the random class returns a randomly selected element from the specified sequence which in this case is the list, "prizes_winner"
            prize = random.choice(prizes_winner) 
            # Used concatenation to print out statements 
            print("As " + player_1 + " is the winner of this game, they will win a prize! Prize will be randomly selected!")
            print("***Prizes are Generating***")
            print("***Prize Generated and Selected***")
            input("***Press Enter to Display your prize!***")
            print("Winning Prize for " + player_1 + ": " + prize)
            
            # Fun questionaire feature which allows either player to answer 3 fun questions about themself.
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                             𝐅𝐔𝐍 𝐐𝐔𝐄𝐒𝐓𝐈𝐎𝐍𝐍𝐀𝐈𝐑𝐄                                ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            print("Everyone who plays our game is a winner! Feel positive by answering a few fun questions!")
            
            # Question 1 - Input + Response 
            q1 = input("Where would you like to travel for your dream vacation?: ")
            print("Wow! " + q1 + " is such a beautiful place! I would love to travel there!")
            # Question 2 - Input + Response
            q2 = input("What's your favourite animal?: ")
            print("I agree! " + q2 + " are awesome!")
            # Question 3 - Input + Response
            q3 = input("What's you favourite ice cream flavour?: ")
            print("Really! " + q3 + " is my favourite ice cream flavour too!")
            
            # Game summary is printed which inclues the total number of rounds played, won by player 1, won by player 2, and rounds tied
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                              𝐆𝐀𝐌𝐄 𝐒𝐔𝐌𝐌𝐀𝐑𝐘                                   ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            print("Total Number of Rounds Played: " + str(total_rounds) + " Rounds")
            print("Total Rounds Won by " + player_1 + ": " + str(p1_rounds) + " Rounds")
            print("Total Rounds Won by " + player_2 + ": " + str(p2_rounds) + " Rounds")
            print("Total Tied Rounds: " + str(tie_rounds) + " Rounds")
            print("==============================================================================================")
            
            # After executing the code in this if branch the loop will break as a winner is determined for the game, which is player 1.
            break 
        
        # This elif conditional statement checks to see if player 2 has scored a total of 52 points and likewise if player 1 has scored 0 points. If those conditions result in 
        # a boolean expression that equals to True then player 2 will be declared as the winner of the entire game, and player 1 will be informed that they lost the game. As 
        # an additional, I added a prize feature which randomly selects a prize from the prize list for player 2, the winner. However, since this branch has a possibilty that 
        # player 2 could be Rosie The Robit, the Robot won't be allowed to win a prize. Another feature is added which allows the user to answer a fun questionaire! 
        # A game summary will also be printed. After this is executed the loop will break. 
        elif player_1_points == 0 and player_2_points == 52:
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                                 𝐑𝐄𝐒𝐔𝐋𝐓𝐒                                       ♠ ♣ ♥ ♦")
            print("==============================================================================================")             
            # Prints out the winner and loser of the game using concatenation and typecasting.
            print("Congratulations, " + player_2 + "! You Won the Game With 52 Points!")
            print("Sorry, " + player_1 + "! You Lost the Game! Better Luck Next Time!")
            
            
            """
            The prize feature will go through an if-else statement to check if player 2 is Rosie The Robot or not. Since Rosie is a Robot it wouldn't make sense for it to be
            able to win a prize. If player 2 is not Rosie the Robot, player 2 will be able to win a prize. Else, player 2 will not win a prize because this means that the 
            player is Rosie The Robot 
            """ 
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                                  𝐏𝐑𝐈𝐙𝐄𝐒                                        ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            if player_2 != "Rosie The Robot":
                # Prize feature which allows player 2, the winner in this condition, to win a random prize.
                
                # Intializing a variable that stores a list of 4 different possible prizes the winner can win
                prizes_winner = ['$10 Tim Horton\'s Gift Card', 'Apple Watch SE', '$20 iTunes Gift Card', '$30 Amazon Gift Card']
                # Intializing a variable that stores the prize selected by the choice function in the random class. 
                # The choice method in the random class returns a randomly selected element from the specified sequence which in this case is the list, "prizes_winner"
                prize = random.choice(prizes_winner) 
                # Used concatenation to print out statements
                print("As " + player_2 + " is the winner of this game, they will win a prize! Prize will be randomly selected!")
                print("***Prizes are Generating***")
                print("***Prize Generated and Selected***")
                input("***Press Enter to Display your prize!***")
                print("Winning Prize for " + player_2 + ": " + prize)
            else:
                print("Prizes were not awarded as Rosie The Robot was the winner.")
                
                
            # Fun questionaire feature which allows either player to answer 3 fun questions about themself.  
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                             𝐅𝐔𝐍 𝐐𝐔𝐄𝐒𝐓𝐈𝐎𝐍𝐍𝐀𝐈𝐑𝐄                                ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            print("Everyone who plays our game is a winner! Feel positive by answering a few fun questions!")
            # Question 1 - Input + Response
            q1 = input("Where would you like to travel for your dream vacation?: ")
            print("Wow! " + q1 + " is such a beautiful place! I would love to travel there!")
            # Question 2 - Input + Response
            q2 = input("What's your favourite animal?: ")
            print("I agree! " + q2 + " are awesome!")
            # Question 3 - Input + Response
            q3 = input("What's you favourite ice cream flavour?: ")
            print("Really! " + q3 + " is my favourite ice cream flavour too!")            
            print("----------------------------------------------------------------------------------------------")
            
            # Game summary is printed which inclues the total number of rounds played, won by player 1, won by player 2, and rounds tied
            # Subheading
            print("==============================================================================================")
            print("♠ ♣ ♥ ♦                              𝐆𝐀𝐌𝐄 𝐒𝐔𝐌𝐌𝐀𝐑𝐘                                   ♠ ♣ ♥ ♦")
            print("==============================================================================================")
            print("Total Number of Rounds Played: " + str(total_rounds) + " Rounds")
            print("Total Rounds Won by " + player_1 + ": " + str(p1_rounds) + " Rounds")
            print("Total Rounds Won by " + player_2 + ": " + str(p2_rounds) + " Rounds")
            print("Total Tied Rounds: " + str(tie_rounds) + " Rounds")
            print("==============================================================================================")
            
            # After executing the code in the if branch the loop will break as a winner is determined for the game, which is player 2.
            break
        
        
        # This else branch is executed in the case that the condition for the if branch and the elif branch above resulted in a boolean value of False. This means that the game
        # did not finish as both player 1 or player 2 did not reach the maximum number of points (52), meaning they are not ready to be declared as winners. Which is why this 
        # else branch is here; it will help continue the rounds until a winner IS reached. Inside of this else branch there are random number generators and nested if-elif-else statments.
        
        # First, 2 random numbers will be generated and stored in variables that will be used later, the total number of rounds will also start to increment by 1. It will then go through
        # the conditional statments. If the random number for player 1 is greater than the random number for player 2, then player 1 wins the round and gains a point and player 2 loses 
        # a point. Score and Round counters will be incremented accordingly. Else if the random number for player 1 is less than the random number for player 2, then player 2 wins the round
        # and gains a point and player 1 loses a point. Score and Round counters will be incremented accordingly. If both of those conditions are not met it will move onto the Else branch 
        # which will only occur if both of the random numbers generated are the same. In this branch, both players will be informed that it is a tie and no one will loose or gain points.
        # Round counters will be incremented accordingly.
        
        else:
            # Random Number Generators 
            # Intializes 2 seperate variables that stores a random integer from the range 1-10 inclusive. One variable for player 1 and the other for player 2.
            # Numbers are generated randomly meaning that the game revolves around luck/chance. 
            player_1_num = random.randint(1,10)
            player_2_num = random.randint(1,10)
            
            # The counter for the total number of rounds is incremented by 1 because the else branch is being executed and this branch continues the rounds in the game. 
            # It is outside the nested if-elif-else statements because it is a counter for the TOTAL number of rounds not just for player 1, player 2, or for ties. 
            total_rounds += 1
            
            # Prints out what round the players are on. Used concantenation and typecasting as the variable is an integer. 
            print("✸✸✸✸✸✸✸✸✸✸")
            print("ROUND " + str(total_rounds))
            print("✸✸✸✸✸✸✸✸✸✸")
            
            
            """
            The if conditional statement checks to see if the random number generated for player 1 is greater than the random number generated for player 2. If the condition
            results in a boolean expression that equals to True then the counter for rounds won by player 1 will be incremented by 1. Then, player 1 will be declared as the winner 
            for that specific round and gain a point, and player 2 will be informed that they lost the round and will loose a point. The score for both players will be printed.
            """
            if player_1_num > player_2_num:
                # Counter for total number of rounds won by player 1 will be incremented by 1 
                p1_rounds += 1
                
                # Prints out the random number generated for each player. Used concatenation and typecasting    
                print(player_1 + " got a " + str(player_1_num))
                print(player_2 + " got a " + str(player_2_num) + "\n")
                
                
                # Prints out player 1 won a point and player 2 lost a point since we are in the conditional branch that only executes if player 1 won. Used concatenation. 
                print(player_1 + " won a point!")
                print(player_2 + " lost a point!" + "\n")
                
                
                # Counter for player 1's score is incremented by 1 and counter for player 2's score is decremented by 1
                player_1_points += 1
                player_2_points -= 1
                
                # Prints out the score for each player and lets them know who won the round. 
                print(player_1 + "'s Score: " + str(player_1_points))
                print(player_2 + "'s Score: " + str(player_2_points))
                print(player_1 + " Wins This Round!")
                print("----------------------------------------------------------------------------------------------")
                
                # After executing the code in this if branch the loop will continue back to the top to check if any player has won after the round. 
                # If no player has won it will come back to the else branch as a winner is not determined for the game
                continue
            
            # The elif conditional statement checks to see if the random number generated for player 1 is less than the random number generated for player 2. If the condition
            # results in a boolean expression that equals to True then the counter for rounds won by player 2 will be incremented by 1. Then, player 2 will be declared as the winner 
            # for that specific round and gain a point, and player 1 will be informed that they lost the round and will loose a point. The score for both players will be printed.
            elif player_1_num < player_2_num:
                # Counter for total number of rounds won by player 2 will be incremented by 1
                p2_rounds += 1
                
                # Prints out the random number generated for each player. Used concatenation and typecasting    
                print(player_1 + " got a " + str(player_1_num))
                print(player_2 + " got a " + str(player_2_num) + "\n")
                
                
                # Prints out player 1 lost a point and player 2 won a point since we are in the conditional branch that only executes if player 2 won. Used concatenation.    
                print(player_1 + " lost a point!")
                print(player_2 + " won a point!" + "\n")
                
                
                # Counter for player 1's score is decremented by 1 and counter for player 2's score is incremented by 1    
                player_1_points -= 1
                player_2_points += 1
                
                # Prints out the score for each player and lets them know who won the round.
                print(player_1 + "'s Score: " + str(player_1_points))
                print(player_2 + "'s Score: " + str(player_2_points))
                print(player_2 + " Wins This Round!")
                print("----------------------------------------------------------------------------------------------")
                
                # After executing the code in this if branch the loop will continue back to the top to check if any player has won after the round. 
                # If no player has won it will come back to the else branch as a winner is not determined for the game    
                continue
            
            # The else conditional statement checks to see if the random number generated for player 1 is equal to the random number generated for player 2. If the condition
            # results in a boolean expression that equals to True then the counter for rounds tied will be incremented by 1. Then, nobody will be declared as the winner or loser 
            # of the round and no one will win or loose a point. The score for both players will be printed.
            else:
                # Counter for total number of rounds tied will be incremented by 1
                tie_rounds += 1
                
                # Prints out the random number generated for each player. Used concatenation and typecasting 
                print(player_1 + " got a " + str(player_1_num) + "\n")
                print(player_2 + " got a " + str(player_2_num) + "\n")
                
                
                # Prints that it is a tie
                print("Nobody Won or Lost a Point!")
                
                
                # Prints out the score for each player and lets them know its a tie.
                print(player_1 + "'s Score: " + str(player_1_points))
                print(player_2 + "'s Score: " + str(player_2_points))
                print("It's a Tie!")
                print("----------------------------------------------------------------------------------------------")
                
                # After executing the code in this if branch the loop will continue back to the top to check if any player has won after the round. 
                # If no player has won it will come back to the else branch as a winner is not determined for the game
                continue 
                # The function ends here! This function will only be executed once called!




# Introduction to the players 
# Heading
print("==============================================================================================")
print("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ")
print("                                𝐕𝐈𝐑𝐓𝐔𝐀𝐋 𝐖𝐀𝐑 𝐂𝐀𝐑𝐃 𝐆𝐀𝐌𝐄")
print("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ")
print("==============================================================================================")

print("Hello Players! Welcome to the Game, War!")

# Asks the user if they would like to play the game. 
user_play = input("Would you like to play the game? ('Yes'/'No') : ")

# This while loop executes if the user wants to play the game. The condition is checked using a logical operator. 
while user_play == "Yes":
    # The if branch will only be executed if the user wants to play the game
    if user_play == "Yes":
        print("Since you want to play, here are the game rules!")
        
        # Game Rules
        # Subheading
        print("==============================================================================================")
        print("♠ ♣ ♥ ♦                               𝐆𝐀𝐌𝐄 𝐑𝐔𝐋𝐄𝐒                                     ♠ ♣ ♥ ♦")
        print("==============================================================================================")
        print("✸ The game deals out 52 points evenly between 2 players, 26 points per player.")
        print("✸ Each player draws a number to play, ranging from 1-10 using our Random Number Generator")
        print("✸ The player with the highest number in each round is given a point, and the player \n   with the lowest number loses a point")
        print("✸ In the case of a tie, where both players draw the same number, no one will win or \n   loose a point")
        print("✸ The game continues until one player scores the maximum number of points and wins. \n   The first player to win 52 points wins the entire game!")

        
        # Asks the user if they want to play against Rosie The Robot or a friend. These are the two options for player 2
        # Subheading
        print("==============================================================================================")
        print("♠ ♣ ♥ ♦                                𝐏𝐋𝐀𝐘𝐄𝐑𝐒                                        ♠ ♣ ♥ ♦")
        print("==============================================================================================")
        player_vs = int(input("Would you like to play against 'Rosie The Robot' or a friend? \nEnter 0 for 'Rosie The Robot' or 1 for friend: "))
        
        # Since player 1 is always going to be the same and has no options like player2 does, the user will be asked to enter the name for the first player
        player_1 = input("Please type in the first player’s name: ")
        
        # This if-else code is for player 2. If the player 1 wants to play against Rosie The Robot then player 2 will be hard coded to Rosie The Robot.  
        # Else, we know the player wants to play with a friend in which they will be prompted to enter the name for the second player. 
        
        # If branch will be executed if user enters a 0 which means that they want to play against Rosie The Robot
        if player_vs == 0:
            # Intialize player 2 to be Rosie the Robot
            player_2 = "Rosie The Robot"
            # Inform users who the players are 
            print("----------------------------------------------------------------------------------------------")
            print("Player 1: " + player_1)
            print("Player 2: Rosie The Robot")
            print("----------------------------------------------------------------------------------------------")
            # Placed this input statement so that the user can read who the players are
            input("Press 'Enter' to continue: ") 
            
        # Else branch will be executed if the if branch is not executed. This only happens when the user enters 1 meaning that they want to play against a friend 
        else: 
            # User will be prompted to enter a name for the second player
            player_2 = input("Please type in the second player’s name: ")
            # Inform users who the players are
            print("----------------------------------------------------------------------------------------------")
            print("Player 1: " + player_1)
            print("Player 2: " + player_2)
            print("----------------------------------------------------------------------------------------------")
            # Placed this input statement so that the user can read who the players are
            input("Press 'Enter' to continue: ") 
        
        # Now that we know the user wants to play the game, and we know who the 2 players are we can call our function that holds the core of the game. 
        # This takes them through the start to the end of the game
        war_card_game()
        
        # Asks the user if they would like to play again. If they say yes they will continue back up to the while loop where the game will be repeated. 
        # Else they will be exited out of the game
        user_play = input("Would you like to play again? ('Yes'/'No') : ")
        
        # If player wants to play again then it will continue back up to the while loop
        if user_play == "Yes":
            continue
        # Executed if the players don't want play again. Will be prompted to give a rating, it will then break out of the loop 
        else:
            print("Players have exited the game! Thanks for playing!")
            user_rating = int(input("Please rate our online card game from 1-5 stars: "))
            print("Thank you! Please give us a detailed feedback on our website at www.onlinewarcardgame.ca!")
            break

# This if statment is if the user said that they don't want to play the game when they were first asked. Since the while loop does not check for this I had to create this if statement
if user_play == "No":
    print("Alright! Thanks for visiting our Game! Goodbye!")
    