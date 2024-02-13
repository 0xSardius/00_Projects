print("Welcome to my Astrology Quiz Game!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Great! Let's play :)")
score = 0

answer = input("What is the ruling planet of Aries? a) Venus b) Mars c) Jupiter d) Saturn ")

if answer.lower() == "mars" or answer.lower() == "b":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

# make a block for the ruling planet of Taurus
answer = input("What is the ruling planet of Taurus? a) Venus b) Mercury c) Jupiter d) Uranus ")

if answer.lower() == "venus" or answer.lower() == "a":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    score -= 1

# make a block for the ruling planet of Gemini
answer = input("What is the ruling planet of Gemini? a) Mercury b) Moon c) Saturn d) Uranus ")

if answer.lower() == "mercury" or answer.lower() == "b":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    score -= 1

# make a block for the ruling planet of Cancer
answer = input("What is the ruling planet of Cancer? a) Jupiter b) Mercury c) Mars d) Moon ")

if answer.lower() == "moon" or answer.lower() == "d":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    score -= 1

# make a block for the ruling planet of Leo
answer = input("What is the ruling planet of Leo? a) Sun b) Venus c) Mars d) Jupiter ")

if answer.lower() == "sun" or answer.lower() == "a":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    score -= 1

print("Thank you for playing! You got " + str(score) + " questions correct!")

