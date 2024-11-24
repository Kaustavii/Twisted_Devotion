def welcome_message():
  print("Welcome to Twisted Devotion")
  print("INSTRUCTIONS: \n - Must input options we give. \n - No inappropriate names. \n - Try not to die!")
  print("You wake up and it’s a normal day. You get dressed and ready for work, quickly grabbing your keys and getting ready to leave.")

def choose_gender():
  response = input("Would you like to be a boy or girl? [girl or boy]: ").lower()
  if response in ["boy", "girl"]:
      name = input("What is your character's name? : ")
      return name, response
  else:
      print("Please choose a valid option: boy or girl.")
      return choose_gender()

def coffee_shop(score, gender):
  response1 = input("Do you want to go to the coffee shop? [yes or no]: ").lower()
  if response1 == "no":
      print("You go to work and live the same life every day.")
      score -= 5
  elif response1 == "yes":
      if gender == "boy":
          print("You drive to your normal coffee shop and see someone new sitting inside. You think she is very pretty and are contemplating talking to her.")
      else:  # For girl
          print("You get to the coffee shop and there's someone there that you have never seen before. You notice him looking at you, and you see him start to walk over to you.")
      score += 5
  else:
      print("Please respond with 'yes' or 'no'.")
      return coffee_shop(score, gender)
  return score

def talk_to_baddie(score, gender):
  if gender == "boy":
      response2 = input("Do you talk to the baddie? [yes or no]: ").lower()
      if response2 == "yes":
          print("You guys seem to be hitting it off very well. After talking for a while, she asks you on a date.")
          score += 5
      elif response2 == "no":
          print("You don't talk to the baddie and repeat this forever.")
          score -= 5
      else:
          print("Please respond with 'yes' or 'no'.")
          return talk_to_baddie(score, gender)
  else:  # For girl
      response2 = input("Do you talk to the mystery man? [yes or no]: ").lower()
      if response2 == "yes":
          print("You and the mystery man, who you found out is named Dorion, really seem to hit it off. After talking for a while, he asks you on a date.")
          score += 5
      elif response2 == "no":
          print("You don't talk to the mystery man and repeat this forever.")
          score -= 5
      else:
          print("Please respond with 'yes' or 'no'.")
          return talk_to_baddie(score, gender)
  return score

def _date(score):
  response3 = input("Do you say yes? [yes or no]: ").lower()
  if response3 == "yes":
      print("You get ready for the date. You start feeling a little weird about going.")
      score += 5
  elif response3 == "no":
      print("You stay home and live the same life every day, YOU LOST.")
      score -= 5
      return score
  else:
      print("Please respond with 'yes' or 'no'.")
      return go_on_date(score)
  return score

def date_experience(score, gender):
  response4 = input("Do you end up going on the date? [yes or no]: ").lower()
  if response4 == "yes":
      if gender == "girl":
          print("The date doesn’t seem to be going very well, and something about him seems off. \n"
                "The dessert comes out, and he gets up to use the restroom. You quickly get out a vial of poison and add a couple drops to his dessert. He seems to be okay after eating,\n"
                "but collapses in the parking lot while you guys are trying to leave.")
      else:
          print("The date goes well, and you enjoy your time together.")
      score += 5
  elif response4 == "no":
      print("You stay home and live the same life every day, YOU LOST.")
      score -= 5
  else:
      print(" 'yes' or 'no'.")
      return date_experience(score, gender)
  return score

def _body(score):
  response5 = input("How do you dispose of the body? [throw in the lake / put it in the road]: ").lower()
  if response5 == "throw in the lake":
      print("You get away with it scotch free.")
      score += 5
  elif response5 == "put it in the road":
      print("You get caught guilty and charged life in prison.")
      score -= 5
  else:
      print("WRONG option. Choose 'throw in the lake' or 'put it in the road'.")
      return _body(score)
  return score


welcome_message()
name, gender = choose_gender()
score = 0
score = coffee_shop(score, gender)
if score >= 0:
  score = talk_to_baddie(score, gender)
if score >= 0:
  score = _date(score)
if score >= 0:
  score = date_experience(score, gender)
if score >= 0 and gender == "girl":
  score = _body(score)

print(f"Your final score is: {score}")