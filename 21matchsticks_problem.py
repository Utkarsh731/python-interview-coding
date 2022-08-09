'''21 sticks problem:
first the opponent will pickup the stick-
minimumsticks = 1,
maximum = 4,
then you will pickup the stick.
the one picking up the last stick will be loser
write a code that will ensure that you will never loose
'''


def game():
    total_sticks = 21
    minimum_sticks = 1 
    maximum_sticks = 4
    while(total_sticks>0):
        user_pickup = int(input("pickup sticks between 1 to 4 = "))
        if user_pickup<minimum_sticks and user_pickup>maximum_sticks:
            return "please pickup between 1 to 4"
        total_sticks = total_sticks - user_pickup
        if total_sticks<1:
            print("you loose")
            break
        system_picks = 5 - user_pickup
        print("system pickup = ", system_picks)
        total_sticks = total_sticks - system_picks
        print("sticks remaining = ",total_sticks)
game()
        
            
        
