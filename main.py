import random
from os import system, name

def clear():
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system('clear')
def start():

  clear()
  print("Teddy's MadLibs \n")
  print("It's normal to be asked the same question multiple times,\njust answer differently each time.\n")

  # Variables Defined with placeholder value
  per1 = "a"
  adj1 = "a"
  adv1 = "a"
  nou1 = "a"
  adv2 = "a"
  per2 = "a"
  nou2 = "a"
  inf1 = "a"
  
  # Randomly Shuffles Variables
  rng = [1,2,3,4,5,6]
  random.shuffle(rng)
  # Add input here
  i = -1
  while i <= 5:
    i += 1
    if i == 6:
      rng.append(str(7))
    if rng[i] == 1:
      per1 = input("Input a Person: ")
    elif rng[i] == 2:
      adj1 = input("Input an Adjective: ")
    elif rng[i] == 3:
      adv1 = input("Input an Adverb: ")
    elif rng[i] == 4:
      nou2 = input("Input a Place: ")
    elif rng[i] == 5:
      adv2 = input("Input a Adjective: ")
    elif rng[i] == 6:
      inf1 = input("Input an Infinitive (e.g to run)")
    else:
      break


    # These Questions are Dependent of Eachother, therefore they are asked later to make re they 
  nou1 = input("Input a Place: ")
  per2 = input("Input a Person who works at the Place: ")
  # Add Madlib Inputs to Array
  # Each Part of the 2D Array is used to define a different line
  madlib1 = []
  madlib2 = []
  madlib3 = []
  madlib2d = [madlib1,madlib2,madlib3]
  madlib1.append(str(per1))
  madlib1.append(str(adj1))
  madlib1.append(str(adv1))
  madlib1.append(str(nou1))
  madlib2.append(str(adv2))
  madlib2.append(str(per2))
  madlib2.append(str(nou2))
  madlib3.append(str(per1))
  madlib3.append(str(inf1))
  # Print Final Story
  print("\nThe", madlib2d[0][1], madlib2d[0][0], "ran", madlib2d[0][2], "to", madlib2d[0][3] + ".")
  print("Consequently, the", madlib2d[1][0], madlib2d[1][1], "threw him to", madlib2d[1][2]+ ".")
  print("In the end,", madlib2d[2][0], "decided", madlib2d[2][1] + ".")

  def choose():
    choose = input("\nWould you like to play again? ")
    if choose.lower() == "yes":
      start()
    elif choose.lower() == "no":
      exit("Done!")
    else:
      print("\nAnswer is Invalid!")
  choose()
start()
