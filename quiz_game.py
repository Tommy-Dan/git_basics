print("Welcome to my computer game!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
print("Okay Let's play :)")
answer = input("What does the CPU stands for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("Please guess again: ")