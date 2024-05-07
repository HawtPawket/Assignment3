# Task 1: Code Correction

# You are provided with a Python script that is supposed 
# to help in event planning, but it has errors. Identify and fix them.



attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Venue Selection

# Based on the corrected code from Task 1, further 
# enhance the program to recommend additional facilities like "audio system"
# or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
print("audio system") if attendees > 100 else print("projector")



# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise 
# recommend "Gourmet Meals Caterers".



attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
print("audio system") if attendees > 100 else print("projector")

food = input("Would you like Vegetarian food")

if food == "yes":
    print("I recommend Veggie Delight Caterers")
if food =="no":
    print("I recommend Gourmet Meals Caterers")




