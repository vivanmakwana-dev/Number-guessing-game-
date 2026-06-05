#Guess the number

import random

number = random.randint(1,50)

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
    guess = int(input("Guess your number between 1 and 50 :-"))
     
    if guess < number:
        print(random.choice(low_messages))
    elif guess > number:
        print(random.choice(high_messages))
    else:
        print(" Finally you guessed correct number!!Huh it was your luck brat")
