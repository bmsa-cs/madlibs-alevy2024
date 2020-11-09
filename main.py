"""
MadLibs
Author: Alex Levy
Period/Core: Core 3


"""
print("Let's play Silly Sentences!")
#this is setting variables for the different parts of the story so they can later be added into the madlib
animal_1 = input("Enter an animal: ")
adjective_1 = input("Enter an adjective: ")
place = input("Enter a noun: ")
occupation = input("Enter an occupation: ")
adjective_2 = input("Enter an adjective: ")
animal_2 = input("Enter an animal: ")
noun_2 = input("Enter a noun: ")
noun_Plural = input("Enter a plural noun: ")
adjective_est = input("Enter an adjective that ends in est: ") 
verb_ing_2 = input("Enter a verb that ends in ing: ")
noun_3 = input("Enter a noun: ")

#this is the first paragraph of the madlib
print(f"\n\nI want to get a {animal_1} but every time I go to buy one I see something very {adjective_1}. Hey, that’s {place}'s pet store for you!")
#this is the second paragraph of the madlib
print(f"\nWhen I got to the pet store I saw the animals were all {verb_ing_2}. Suddenly a nearby", end= ' ')
print(adjective_2, "" + occupation, end= '')
print(f" runs out of the store holding a {animal_2}! From the corner of my eye, I watched the {occupation} come back in and grab a {noun_2} too.")
#this is the third paragraph of the madlib
print(f"\nI walk around the store and look at all of the {noun_Plural} around me. All of a sudden, I see the", end= ' ')
print(adjective_est, "" + animal_1, end= '')
print(f" I’ve ever seen! I want to take it home but it’s hard to catch it because it keeps, {verb_ing_2} away from me! I finally catch it and pay for it with some spare {noun_3}. I head home with my new {animal_1} safe and sound.")
