print("Title of program: Simple math Revision")
print()
print("Welcome to this wonderful math revision website! Please answer the following questions truthfully and you to test your math calculation skills!")
print("Please respond with an answer, for example, if you think the answer is 100, type 100 for that specific question. All the best!")
print()
points = 0
Question1 = int(input("what is the answer for 25 x 5?"))
if Question1 == 125:
  print("Great!")
  points += 1
else:
  print("Oops! Your answer is wrong")

Question2 = int(input("what is the answer for 23x5-(70-1)?"))
if Question2 == 46:
  print("Great Job!")
  points += 1
else:
  print("Oops! Your answer is wrong")

Question3 = int(input("what is the answer for 34-67+689+(69x3)?"))
if Question3 == 863:
  print("Yay! You got it correct!")
  points += 1
else:
  print("Oops! Your answer is wrong") 

Question4 = int(input("What is the answer for 68x2-(88/4+2)+995? (/means divide)"))  
if Question4 == 133:  
  print("Yay! You got it correct!")
  points += 1
else:
  print("Oops! Your answer is wrong") 

Question5 = int(input("What is the answer for 69+111+(629x4)?"))
if Question5 == 2696: 
  print("Hooray! You did it!")
  points += 1
else:
  print("Oops! Your answer is wrong")

Question6 = int(input("What is the answer for 45+332-38+(4545/9)-22x3+95x4? (/ means divide)
if Question6 == 1158:
  print("Yay, you have done it!")
  points += 1
else:
  print("Oops! Your answer is wrong")
  
print("You got " + str(points) + " / 5 !")
if points == 5:
  print("WooHoo! Great Job! Keep it up!")
else:
  print("Try better next time")


  
