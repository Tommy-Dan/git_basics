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

answer = input("What does the GPU stands for? ")
if answer == "Graphics Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("Please guess again: ")

answer = input("What does the RAM stands for? ")
if answer == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")
    print("Please guess again: ")

answer = input("What does the PSU stands for? ")
if answer == "Power Supply Unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("Please guess again: ")

answer = int(input("How many megabytes make a gigabyte? "))
if answer == 1000:
    print("Correct!")
else:
    print("Incorrect!")
    print("Please guess again: ")