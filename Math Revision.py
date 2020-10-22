print("Title of program: Simple math Revision")
print()
print("Welcome to this wonderful math revision website! Please answer the following questions truthfully and you to test your math calculation skills!")
print("Please respond with an answer")
print()
points = 0
Question1 = int(input("what is the answer for 25 x 5?"))
if Question1 == 125:
  print("Great!")
  points += 1
else:
  print("Oops! Try again")

Question2 = int(input("what is the answer for 23x5-(70-1)?"))
if Question2 == 46:
  print("Great Job!")
  points += 1
else:
  print("Oops! Try again")

Question3 = int(input("what is the answer for 34-67+689+(69x3)?"))
if Question3 == 863:
  print("Yay! You got it correct!")
  points += 1
else:
  print("Oops! Try again") 

Question4 = int(input("What is the answer for 68x2-(88/4+2)+995? (/means divide)"))  
if Question4 == 133:  
  print("Yay! You got it correct!")
  points += 1
else:
  print("Oops! Try again") 

Question5 = int(input("What is the answer for 69+111+(629x4)?"))
if Question5 == 2696: 
  print("Hooray! You did it!")
  points += 1
else:
  print("Oops! Try again") 
print("You got " + str(points) + " / 5 !")  

  
