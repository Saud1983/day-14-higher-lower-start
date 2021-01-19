from random import randint
from art import logo,vs
from game_data import data
from replit import clear

game=True
score=0

def new_selection():
  dictionary_len=len(data)
  selection=randint(0,dictionary_len-1)
  # print(dictionary_len)
  element=data[selection]
  data.remove(element)
  return element

compair_list=[]

temp_element=new_selection()
compair_list.append(temp_element)
temp_element=new_selection()
compair_list.append(temp_element)
print(logo)

while game:

  for i in range(0,2):
    name=compair_list[i]["name"]
    follower=compair_list[i]["follower_count"]
    desciption=compair_list[i]["description"]
    country=compair_list[i]["country"]
    if i==0:
      print(f"Compare A: {name},{desciption}, from {country}")
    else:
      print(vs +" \n")
      print(f"Against B: {name},{desciption}, from {country}")
  
  answer=input("Who has more followers? Type 'A' or 'B': ").lower()
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
  
  new_selection()
  temp_element=new_selection()
  compair_list.append(temp_element)
  clear()
  print(logo)
  if correct==1:
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")