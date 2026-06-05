#Guess the number

import random

number = random.randint(1,50)
tries = 0
low_messages = [ 
    "You are such great loser huh?" ,
    "Skill issue detected",
    "Congratulations!! you guessed the wrong number" ,
    "The number is laughing at you",
    "Too low just like your IQ"
]

high_messages = ["Too high ! Try again.",
                 "The number isn't on mars",
                 "still you are a loser ",
                 "You donkey!!!"
]
while True:
    try:
        guess = int(input("Guess a number between 1 and 50: "))
    except ValueError:
        print("Are you a donkey ? Enter a valid number you stupid.")
        continue

    if not 1 <= guess <= 50:
        print("are you blind or what? Don't you see that number must be  between 1 and 50 ")
        continue

    tries += 1
    
     
    if guess < number:
        tries +=1
        print(random.choice(low_messages))
    elif guess > number:
        tries +=1
        print(random.choice(high_messages))
    else:
        tries +=1
        print(" Finally you guessed correct number!!Huh it was your luck brat")
        print(f"Literally you took {tries} attempts such a loser!") 
        break
