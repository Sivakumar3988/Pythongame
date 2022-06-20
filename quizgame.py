print("welcome to my laptop game")

playing=input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()
print("okay! lets play :)") 
score = 0

answer = input("what idoes cpu stand for? ")
if answer.lower() == "central processing unit": 
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stand for? ")
if answer.lower() == "graphic processing unit": 
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does Ram stand for? ")
if answer.lower() == "random access memory": 
    print("correct")
    score += 1
else:
    print("incorrect!")  
answer = input("what idoes lpu stand for? ")
if answer == "Lovely professional unit": 
    print("correct")
    score += 1
else:
    print("incorrect!")  
print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
