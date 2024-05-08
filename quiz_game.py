print("Welcome to my computer game!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
print("Okay Let's play :)")
score = 0

answer = input("What does the CPU stands for? ")
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the GPU stands for? ")
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the RAM stands for? ")
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the PSU stands for? ")
if answer == "Power Supply Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = int(input("How many megabytes make a gigabyte? "))
if answer == 1000:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")