from random import randint
from art import logo,vs
from game_data import data
from replit import clear

# to activate the while loop
game=True

#player score
score=0

# function to randomly select an element from data list and delete that selected element
def new_selection():
  dictionary_len=len(data)
  selection=randint(0,dictionary_len-1)
  # print(dictionary_len)
  element=data[selection]
  data.remove(element)
  return element

# A list for use later that selected element from function can be appended to this list which contains tow element only at a time
compair_list=[]

# To populate compair_list with 2 elements in the first run of the program, which occour one time only
temp_element=new_selection()
compair_list.append(temp_element)
temp_element=new_selection()
compair_list.append(temp_element)

# To print the game logo once when starting the program
print(logo)

# To start the game
while game:

# To loop tow times for showing the data from both elements in the compair_list
  for i in range(0,2):
    name=compair_list[i]["name"]
    follower=compair_list[i]["follower_count"]
    desciption=compair_list[i]["description"]
    country=compair_list[i]["country"]
    # The first loop fill this string
    if i==0:
      print(f"Compare A: {name},{desciption}, from {country}")
    # The second loop fill this string
    else:
      print(vs +" \n")
      print(f"Against B: {name},{desciption}, from {country}")

  # Ask the player to choose one of those names showing in the previous strings 
  answer=input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check the player answer, if the answer is correct, player will gain 1 score and the first element in the compair_list will be removed and use the correct variable as a filter to print the continuation of the game, othewise the game will be terminated and the filter will select the termination message to be printed
  if answer=="a":
    if compair_list[0]["follower_count"]>compair_list[1]["follower_count"]:
      score += 1
      first_element=compair_list[0]
      compair_list.remove(first_element)
      correct=1
    else:
      game=False
      correct=0
  else:
    if compair_list[1]["follower_count"]>compair_list[0]["follower_count"]:
      score += 1
      first_element=compair_list[0]
      compair_list.remove(first_element)
      correct=1
    else:
      game=False
      correct=0   
  
  # calling the function to select and return an element from the list called data
  new_selection()

  # Add that new element to compair_list to be the second element
  temp_element=new_selection()
  compair_list.append(temp_element)

  # Clear the screen
  clear()

  # Show the game logo
  print(logo)

  # Print a message based on the value of the filter
  if correct==1:
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")