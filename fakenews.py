# Import a random module
import random

# Make lists of subjects,actions,objects
subjects=[
    "Shahrukh Khan",
    "A group of monkeys",
    "A cat in India",
    "Prime Minister",
    "Hania Amir",
    "Ambaani",
    "A boy of Pakistan",
    "Buffaloes of Africa",
    "Antarctica Penguins",
    "Salman Khan",
]
actions=[
    "Sleeps",
    "Eats",
    "Declares",
    "Dances with",
    "Falls in love",
    "Murders",
    "Enjoys",
    "Celebrates",
    "Is chilling",
    "Worked at",
]
objects=[
    "Near Minar-e-Pakistan.",
    "In Lahore Fort.",
    "at Model Bazaar.",
    "a plate of samosa.",
    "chips packet from main bazar.",
    "Noodles.",
    "during PSL Match.",
    "Kuch kuch hota hai movie.",
    "Aeroplane.",
    "At mountains.",
]
print("Welcome to FAKE NEWS HEADLINE GENERATOR.")
# Use while loop to generate multiple headlines until the user says no
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    object=random.choice(objects)

    headline = f"BREAKING NEWS: {subject} {action} {object}"
    print(headline)

    ans=input("Do you want another headline? (yes/no)\n").strip().lower()
    if ans=="no":
        break

print("Thank you for watching our Fake News Headlines!.Have a Fun Day.")    
    
