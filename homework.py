# Exercise #1
# Accept two user ages as inputs and give us the difference between them. 
# (The Answer should always be a positive output)

user1_age = 72
user2_age = 3
if user1_age >= user2_age:
    result = user1_age - user2_age
else:
    result = user2_age - user1_age
print(result)

# Exercise #2
# Accept 3 user inputs for variables named noun, verb and adjective. 
# Print out a formatted string using the outputs.

noun = "The Goonies"
adjective = "greatest"
verb = "die"
print(f" {noun} is the {adjective} movie ever made, and that's a hill I will {verb} on!!!")

# Exercise #3
# Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

age = 67

if age < 18:
    print("Children")

elif age >= 18 and age <= 65:         ### Side note I wasn't sure if ya'll actually want it to ask for the 
    print("Adult")                    ### age but that would just be age = int(input("What is your age"))

else:
    print("Senior")

# Exercise #4
# Take in a number from a user input output the number squared.

num = 21
numsqua = num ** 2
print(numsqua)

# Exercise #5
# Check the below variables' length. If the length of the word is greater than 5 output True,
# if it is less than 5, output False

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

if len(word1) > 5:
    print(True)
else:
    print(False)

if len(word2) > 5:
    print(True)
else:
    print(False)

if len(word3) > 5:
    print(True)
else:
    print(False)

if len(word4) > 5:
    print(True)
else:
    print(False)

if len(word5) > 5:
    print(True)
else:
    print(False)



# Test github