"""
Name: Ebruphihor Blessing Okan
Class: CST 205 100 - Introduction to Programming with Python
Assignment: Module 1 Activity
Date: September 5, 2025
Description: This program demonstrates variables, control flow,
             and collections (list, dictionary, tuple, set).
"""

#Variables and Data Types
frist_name = "Blessing"
last_name = "Okan"
#Lists
hobbies = ["Anime","Reading", "Cooking", ]
#Dictionaries
hobbies_dict = {
    "Anime": ["Clevatess", "The Water Magician", "Demon Slayer"],
    "Reading": ["The King of Wrath", "The Way of Kings", "Leave me behide"],
    "Cooking": ["Kimchi Chigae", "Jollof Rice", "Galbi Jjim"]
}

#Control Flow Examples

#If-statements with list and dictionary
if "Anime" in hobbies: 
    print(f"{frist_name} Likes to watch Anime.")
    print("Anime is one of my favorite hobbies.")
    
if "Reading" in hobbies_dict:
    print(f"{frist_name} Likes to read books.")
    print("Reading is one of my favorite hobbies.")
    
    
#Loop through Dictionary 
if "Anime" in hobbies: 
    print("Anime is one of my favorite hobbies!")


# Tuples Example (Immutable List)
anime_tuple = ("Clevatess", "The Water Magician", "Demon Slayer")

for anime in anime_tuple: 
    print("Anime from tuple:", anime)


  
  





