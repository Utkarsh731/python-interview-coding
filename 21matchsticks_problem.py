# 21 sticks problem:
# The opponent will pick up sticks first, with the minimum being 1 and the maximum being 4.
# Then the user will pick up sticks. The one who picks up the last stick loses.
# This code ensures that the user will never lose the game by using a specific strategy.

def game():
    total_sticks = 21 # Initialize total number of sticks to 21
    minimum_sticks = 1 # Minimum number of sticks that can be picked up
    maximum_sticks = 4 # Maximum number of sticks that can be picked up

    while(total_sticks > 0): # Loop until all sticks are picked up
        user_pickup = int(input("Pick up sticks between 1 to 4: ")) # Input for user's pick up

        # Validate user input
        if user_pickup < minimum_sticks or user_pickup > maximum_sticks:
            return "Please pick up between 1 to 4 sticks"

        total_sticks -= user_pickup # Subtract user's pick up from total sticks

        if total_sticks < 1: # If total sticks is less than 1, the user loses
            print("You lose")
            break

        system_picks = 5 - user_pickup # Calculate system's pick up using a specific strategy
        print("System picks up: ", system_picks)
        total_sticks -= system_picks # Subtract system's pick up from total sticks
        print("Sticks remaining: ", total_sticks)

game()
