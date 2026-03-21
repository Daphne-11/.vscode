inventory = []
hp = 10
 
print('Welcome to the Hidden Garden in Dreamworld!')
print('You will have to find its location before you fall asleep')
print('Are you ready?')
 
 
def scene1():
    print('You have been having weird dreams for a while now...')
    choice = input('Explore the place? (yes/no): ').lower()
 
    if choice == 'yes':
        print('You arrive at a strange beach...')
        scene2()
    elif choice == 'no':
        print('You never wake up.')
        print('GAME OVER')
        scene1()
 
 
def scene2():
    print('You find a small key in the sand.')
    choice = input('Keep the key? (yes/no): ').lower()
 
    if choice == 'yes':
        inventory.append('small key')
        print('Key added to inventory.')
        scene3()
    elif choice == 'no':
        print('You needed that key.')
        print('Why did you throw that key..?')
        print('Suddenly, the moment loops back and forth. The key vanished.')
        print('You turn around, dizzy. There is a weird creature staring at you. It slowly got closer to you...')
        print('GAME OVER')
        scene1()
 
 
def scene3():
    global hp
    print('You look for where to use the key.')
    print('It looks like the entrance to a house.')
    print('You insert the key cautiously. The door opens!')
    print('As you open the door, you peek around. It looks like a garage.')
    print('You see two more doors. One on the left, one on the right.')
    choice = input('Go left or right? (left/right): ').lower()
 
    if choice == 'left':
        print('You found a door. The key works.')
        scene4()
    elif choice == 'right':
        print('Nothing here. You waste time.')
        hp -= 2
        print(f'HP: {hp}')
        scene3()
 
 
def scene4():
    global hp
    print('You enter the hidden garden.')
    print('It is beautiful, just like in your dreams.')
    print('There is a table with food on it. It looks delicious, and you are very hungry.')
    inventory.append('food')
 
    choice = input('Eat the food? (yes/no): ').lower()
 
    if choice == 'yes':
        hp -= 5
        print('You feel sick and sleepy.')
        choice = input('Sleep? (yes/no): ').lower()
 
        if choice == 'yes':
            print('You never wake up.')
            print('GAME OVER')
            scene1()

        if choice == 'no':
            print('You pinch yourself to stay awake. It works, but you feel weak.')
            print('You push through, but you can barely keep your eyes open.')
            print('You hallucinate, and feel strange. You look at your hands...They are vanishing.')
            print('You faded away. GAME OVER')
            scene1()
 
    elif choice == 'no':
        print('You stay alert. Something feels wrong.')
        hp += 2
        scene5()
 
 
def scene5():
    global hp
    print('You look for an exit.')
    choice = input('Where is the door? (back/left/right): ').lower()
 
    if choice == 'back':
        print('Wrong direction.')
        hp -= 3
        print(f'HP: {hp}')
        scene5()
 
    elif choice == 'left':
        print('Something scares you.')
        hp -= 5
        print(f'HP: {hp}')
        scene5()
 
    elif choice == 'right':
        print('You escape.')
        print('It was all a dream...')
 
 
# Start game
scene1()