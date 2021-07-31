print("Welcome to my quiz!")

playing = input("Are you brave enough to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU means? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does GPU means? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM means? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does PSU means? ")
if answer.lower() == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Congratulations! You got " + str((score/4)*100) + "%" + " right answers!")
k=input("press close to exit") 
