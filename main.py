from random import randint
from art import logo,vs
from game_data import data

game=True
start=5


# while not game:
for _ in range(2):
  dictionary_len=len(data)
  selection=randint(0,dictionary_len)
  print(dictionary_len)
  name=data[selection]["name"]
  follower=data[selection]["follower_count"]
  desciption=data[selection]["description"]
  country=data[selection]["country"]
  data.remove(selection)
  if _ == 0:
    print(logo)
    print(f"Compare A: {name},{desciption}, from {country}")
  else:
    print(vs)
    print(f"Against B: {name},{desciption}, from {country}")

answer=input("Who has more followers? Type 'A' or 'B': ")