from secrets import choice


inventory = []
hp = 10


print ('Welcome to the Hidden Garden in Dreamworld!')
print ('You will have to find its location before you fall asleep')
print ('Are you ready?')

def scene2():
    print('You walked around the beach, your name resonated more and more.')
    print('You looked down, at the sand. That is were you saw a small key.')
    print('You kneeled down and picked it up. Where could it possibly be used?')
    choice = input('Are you going to keep the key? (yes/no)')
    if choice == 'yes':
        print('You found a valuable object! Check your inventory!')
        inventory.append('small key')
        scene3()
    elif choice == 'no':
        print('You left the key there. You were very wrong, you have no escape.')
        scene2()

def scene1():
    print('You have been having weird dreams for a while now, it has been a whole month now. You can\'t get that strange sensation off your head when you wake up')
    print('Then one day, while you were hanging out with your friends, you saw a place that looked similar to the entrance of the garden you have been dreaming with.')
    print('You heard a voice calling your name from that place. Telling you to wander around.')

    choice = input('Are you willing to explore that place and find the garden of your dreams? (yes/no)')
    if choice == 'yes':
        print('You got closer to the place. Suddenly, you were in a beach. It does not make sense, but you have to stay calm')
        print('Keep going. Your name is still being called. You have to find where it is coming from')
        scene2()
    elif choice == 'no':
        print('You decide to ignore the voice. You went home, thinking everything was fine.')
        print('But that very night, your dream was not calm.')
        print('You were unable to wake up eversince')
        print('GAME OVER')
        scene1()
scene1() 

def scene3():
    print('You had no idea where the key could be used. Maybe, there is a door nearby?')
    choice = input('Where will you go first? (left/right)')
    if choice == 'left':
        print('You went left, and you found a door. The key fits perfectly!')
        scene4()
    elif choice == 'right':
        print('You went right, but you could not find anything.')
        print('You rumaged around for a while. You have to go back and go to the left')
        hp -= 2
        scene4()
scene3()
  

def scene2():
    print('You walked around the beach, your name resonated more and more.')
    print('You looked down, at the sand. That is were you saw a small key.')
    print('You kneeled down and picked it up. Where could it possibly be used?')
    choice = input('Are you going to keep the key? (yes/no)')
    if choice == 'yes':
        print('You found a valuable object! Check your inventory!')
        inventory.append('small key')
        scene3()
    elif choice == 'no':
        print('You left the key there. You were very wrong, you have no escape.')
        scene2()

def scene4():
    print('You opened the door! You found the hidden garden!')
    print('The garden was soothing and ethereal. You felt just like you were in your dreams.')
    print('You saw a table with food on it. It looked delicious. You grabbed it.')
    inventory.append('Food')
    choice = input('Are you going to eat the food? (yes/no)')
    if choice == 'yes':
        print('It was so good. You ate more and more. But, eating so much made you tired, and you got nauseous after doing so.')
        hp -= 5
        print('You were so tired that you wanted to fall asleep. It felt like the garden embraced you to sleep.')
        choice = input('Will you sleep? (yes/no)')
        if choice == 'yes': 
         print('You slowly closed your eyes and fell asleep without noticing. But, there was something weird, you could not wake up.')
        print('GAME OVER')
        scene1()  

def scene3():
    print('You had no idea where the key could be used. Maybe, there is a door nearby?')
    choice = input('Where will you go first? (left/right)')
    if choice == 'left':
        print('You went left, and you found a door. The key fits perfectly!')
        scene4()
    elif choice == 'right':
        print('You went right, but you could not find anything.')
        print('You rumaged around for a while. You have to go back and go to the left')
        hp -= 2
scene3()
  
def scene5():
    print('Maybe staying in the garden was a bad idea. You have to look for an exit.')
    choice = input('Where was the door? (In the back/Left/right)')
if choice == 'in the back':
    print('You went to the back. The door was not there.')
    hp -= 3
    scene5()
if choice == 'left':
    print('You went left. There was a weird thing. You got so scared you ran away quickly.')
    hp -= 5
    scene5()
if choice == 'right':
    print('The door was on the right. It took you a while to open it, but when you did...')
    print('It was all a dream? You were on your bed, holding your chest, scared')
    print('It happened again... The same dream you had had the nights before. You always forgot it, it felt so real...')


def scene4():
    print('You opened the door! You found the hidden garden!')
    print('The garden was soothing and ethereal. You felt just like you were in your dreams.')
    print('You saw a table with food on it. It looked delicious. You grabbed it.')
    inventory.append('Food')
    choice = input('Are you going to eat the food? (yes/no)')
    if choice == 'yes':
        print('It was so good. You ate more and more. But, eating so much made you tired, and you got nauseous after doing so.')
        hp -= 5
        print('You were so tired that you wanted to fall asleep. It felt like the garden embraced you to sleep.')
        choice = input('Will you sleep? (yes/no)')
        if choice == 'yes': 
         print('You slowly closed your eyes and fell asleep without noticing. But, there was something weird, you could not wake up.')
        print('GAME OVER')
        scene1()

    elif choice == 'no':
        print('You decided not to eat the food. After a few minutes, you noticed how unsettling the garden was.')
        print('Being scared made your heart beat faster. You were so scared all your tiredness went away.')
        hp += 2
        scene5()

def scene5():
    print('Maybe staying in the garden was a bad idea. You have to look for an exit.')
    choice = input('Where was the door? (In the back/Left/right)')
if choice == 'in the back':
    print('You went to the back. The door was not there.')
    hp -= 3
    scene5()
if choice == 'left':
    print('You went left. There was a weird thing. You got so scared you ran away quickly.')
    hp -= 5
    scene5()
if choice == 'right':
    print('The door was on the right. It took you a while to open it, but when you did...')
    print('It was all a dream? You were on your bed, holding your chest, scared')
    print('It happened again... The same dream you had had the nights before. You always forgot it, it felt so real...')



        


    
    
