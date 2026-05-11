#CREATIVITY: Added a "Story Style" selector (Funny or Scary) that changes the narrative
#Author: Gedeon Agougnon
#Course: CSE 121b
#Assignment: W01 Prove - Clever Stories


#1. Ask about the story style (A touch of creativity)
print("Welcome to Gedeon's story Generator!")
style=input("Choose your style story - Enter 1 for funny or Enter 2 for scary:")
print("Please enter the following :\n")

# We create a loop that runs until the user enters 1 or 2
style = ""
while style not in ["1", "2"]:
    style = input("Choose your story style - Enter 1 for funny or 2 for scary: ")
    if style not in ["1", "2"]:
        print("Invalid choice! Please enter only 1 or 2.")
#2. Word Collection

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")

#3. Word Preparation (Formatting)

exclamation_cap = exclamation.capitalize()
adj_low = adjective.lower()
animal_low = animal.lower()

print("\nYour story is:")
print("--------------------------------------------------")

#4. Logic of the story according to the chosen style

if style == "2":
    # Histoire version "Scary" (Effrayante)
    print(f"In the dead of night, I was really in trouble. It all started when I saw a")
    print(f"terrifying {adj_low} {animal_low} {verb1.lower()} in the dark shadows. \"{exclamation_cap}!\"")
    print(f"I screamed. But all I could think to do was to {verb2.lower()} for my life.")
    print(f"Suddenly, it stopped, but not before it tried to {verb3.lower()}")
    print(f"right in front of my trembling family.")
else:
    # Histoire version "Funny" (Drôle - par défaut)
    print(f"The other day, I was really in trouble. It all started when I saw a very")
    print(f"{adj_low} {animal_low} {verb1.lower()} down the hallway. \"{exclamation_cap}!\"")
    print(f"I yelled. But all I could think to do was to {verb2.lower()} over and over.")
    print(f"Miraculously, that caused it to stop, but not before it tried to {verb3.lower()}")
    print(f"right in front of my family.")

print("--------------------------------------------------")
# Une petite touche d'humour pour finir
print("Moral of the story: Never trust a " + animal.lower() + " when you are in a " + adjective.lower() + " mood!")
print("P.S. No " + animal.lower() + "s were harmed in the making of this story. 😂")