import random

class pokemon:
  def __init__(self, name, attack_power, isfriendly = True):
    self.name = name
    self.attack_power = attack_power
    self.isfriendly = isfriendly

  def __repr__(self):
    description = "{self_name} has {attack_power} attack power and is ".format(self_name = self.name, attack_power = self.attack_power)
    if self.isfriendly == True:
      description += "friendly toward other Pokemon!"
    elif self.isfriendly == False:
      description += "unfriendly toward other Pokemon. Be careful!"
    else:
      description += "unsure. Check your Pokemon inputs and try again!"
    return description

  def interact(self, other_pokemon):
    if (other_pokemon.isfriendly == True and self.isfriendly == True):
      # importing random allows us to have as many random, unique interactions between the pokemon as we'd like! The logic will choose out of the list of possible interactions at random.
      friendly_outcomes_list = [
        "{self_name} and {other_pokemon_name} become best friends because they're both friendly <3".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} and {other_pokemon_name} formed more than a friendship... this is... LOVE! <3".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} and {other_pokemon_name} got along pretty well but in a nice acquaintance sort of way".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} cracked a joke and {other_pokemon_name} laughed".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} hopped on top of {self_name}! It looks like they're having fun though!".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
      print(random.choice(friendly_outcomes_list))

    elif (other_pokemon.isfriendly == True and self.isfriendly == False):
      hostile_outcomes_list1 = [
        "{self_name} bullies {other_pokemon_name} because {self_name} is unfriendly".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} glares at {other_pokemon_name}.. {other_pokemon_name} shys away".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} starts launching a flurry of attacks at {other_pokemon_name} who runs top speed to safety!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} runs up to {self_name} with a smile. {self_name} surprise attacks {other_pokemon_name}. {other_pokemon_name} is now unconscious".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} tries to befriend {self_name} who ignores him".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
      print(random.choice(hostile_outcomes_list1))

    elif (other_pokemon.isfriendly == False and self.isfriendly == True):
      hostile_outcomes_list2 = [
        "{other_pokemon_name} bullies {self_name} because {other_pokemon_name} is unfriendly".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} glares at {self_name}.. {self_name} shys away".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} starts launching a flurry of attacks at {self_name} who runs top speed to safety!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} runs up to {other_pokemon_name} with a smile. {other_pokemon_name} surprise attacks {self_name}. {self_name} is now unconscious".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} tries to befriend {other_pokemon_name} who ignores him".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
      print(random.choice(hostile_outcomes_list2))

    elif (other_pokemon.isfriendly == False and self.isfriendly == False):
      print("{self_name} and {other_pokemon_name} start a POKEMON BATTLE!".format(self_name = self.name, other_pokemon_name = other_pokemon.name))
      if (self.attack_power > other_pokemon.attack_power):

        winner_outcomes_list1 = [
        "{self_name} pretends to be friendly but suddenly sneak attacks {other_pokemon_name} for the win! Better luck next time, {other_pokemon_name}!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} dashes toward {self_name} who launches a perfect counter-attack! That was fast.. {self_name} is victorious!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} unleashes a flurry of attacks at {self_name} who dodges everything! {self_name} lands a critical strike to win the battle!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} uses an ultimate ability to win the battle in a single strike! {other_pokemon_name} is KO'd".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} and {other_pokemon_name} exchange a mean look and immediately fight to the death! {self_name} knocks {other_pokemon_name} down to 0 HP who returns to the pokeball!".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
        print(random.choice(winner_outcomes_list1))

      elif (self.attack_power < other_pokemon.attack_power):

        winner_outcomes_list2 = [
        "{other_pokemon_name} pretends to be friendly but suddenly sneak attacks {self_name} for the win! Better luck next time, {self_name}!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} dashes toward {other_pokemon_name} who launches a perfect counter-attack! That was fast.. {other_pokemon_name} is victorious!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} unleashes a flurry of attacks at {other_pokemon_name} who dodges everything! {other_pokemon_name} lands a critical strike to win the battle!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} uses an ultimate ability to win the battle in a single strike! {self_name} is KO'd".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} and {self_name} exchange mean looks and immediately fight to the death! {other_pokemon_name} knocks {self_name} down to 0 HP who returns to their pokeball!".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
        print(random.choice(winner_outcomes_list2))

      elif (self.attack_power == other_pokemon.attack_power):

        draw_outcomes_list = [
        "{other_pokemon_name} quick attacks {self_name} who dodges! The two continue to attack each other but can't seem to land hits- it's a draw!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} and {other_pokemon_name} both charge up for a vicious attack and unleash them at the same time, KO'ing each other at the same time!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{self_name} and {other_pokemon_name} fight each other for hours! The slugfest finally ended in a draw!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} uses their ultimate ability but {self_name} dodges in the nick of time. {self_name} counters but {other_pokemon_name} holds their ground. It's a tie!".format(self_name = self.name, other_pokemon_name = other_pokemon.name),
        "{other_pokemon_name} and {self_name} glare at each other but acknlowedges the other's strength. They return to their Pokeballs.".format(self_name = self.name, other_pokemon_name = other_pokemon.name)
      ]
        print(random.choice(draw_outcomes_list))

      else: print("Uh oh! An error occurred with your pokemon. Try again!")
    else: print("Uh oh! An error occurred with your pokemon. Try again!")

# Welcome message for user
print("Hello! Welcome to the Pokemon Simulator! Here you can see how different Pokemon interact with each other.")


# User input logic for Pokemon 1
pokemon1_name = input("Type the name of the 1st Pokemon you'd like: ")

while True:
  pokemon1_attack_power = input("Input a power level from 0-100 for this Pokemon: ")
  try:
    pokemon1_attack_power = int(pokemon1_attack_power)
  except:
    print("Please input a valid number between 0 and 100")
    continue
  if pokemon1_attack_power >= 0 and pokemon1_attack_power <=100:
    break
  else:
    print("Please input a valid number between 0 and 100")
    continue

while True:
  isfriendly = input("Is this Pokemon friendly? ")
  if isfriendly in ["yes", "Yes", "y", "Y"]:
    isfriendly = True
    break
  elif isfriendly in ["no", "No", "n", "N"]:
    isfriendly = False
    break
  else:
    print("Please answer with 'yes' or 'no'")
    continue

# User input logic for Pokemon 2 (logic identical to Pokemon 1)
pokemon2_name = input("Type the name of the 2nd Pokemon you'd like the 1st Pokemon to interact with: ")

while True:
  pokemon2_attack_power = input("Input a power level from 0-100 for this Pokemon: ")
  try:
    pokemon2_attack_power = int(pokemon2_attack_power)
  except:
    print("Please input a valid number between 0 and 100")
    continue
  if pokemon2_attack_power >= 0 and pokemon2_attack_power <=100:
    break
  else:
    print("Please input a valid number between 0 and 100")
    continue

while True:
  isfriendly2 = input("Is this Pokemon friendly? ")
  if isfriendly2 in ["yes", "Yes", "y", "Y"]:
    isfriendly2 = True
    break
  elif isfriendly2 in ["no", "No", "n", "N"]:
    isfriendly2 = False
    break
  else:
    print("Please answer with 'yes' or 'no'")
    continue

# Intializing Pokemon 1 and Pokemon 2 objects using defined Pokemon class and user input data
pokemon1 = pokemon(pokemon1_name, pokemon1_attack_power, isfriendly)
pokemon2 = pokemon(pokemon2_name, pokemon2_attack_power, isfriendly2)

# Logic for user to make a choice on what to do next (includes validation)
while True:
  user_action = input("""Pokemon Trainer Actions:
  1 - Description of {pokemon1}
  2 - Description of {pokemon2}
  3 - Simulate {pokemon1} and {pokemon2}'s interaction!
      (Try again for a new outcome?)
  4 - Quit game
  """.format(pokemon1=pokemon1.name, pokemon2=pokemon2.name))
  try:
    user_action = int(user_action)
  except:
    print("Please input a valid number between 1 and 4")
    continue
  if user_action >=1 and user_action <=4:
    if user_action == 1:
      print(pokemon1)
      continue
    elif user_action == 2:
      print(pokemon2)
      continue
    elif user_action == 3:
      pokemon1.interact(pokemon2)
      continue
    elif user_action == 4:
      print("Thank you for playing!")
      break
    else:
      print("Uh oh! An error's occurred. Try again!")
      continue
  else:
    print("Please input a valid number between 1 and 4")
    continue
