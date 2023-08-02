# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def trueLove(qName1, qName2):
    combine = qName1 + qName2
    counterTrue = 0
    counterLove = 0
    for letter in combine:
        if (letter.lower() == 't'):
            counterTrue+=1
        elif (letter.lower() == 'r'):
            counterTrue+=1
        elif (letter.lower() == 'u'):
            counterTrue+=1
        elif (letter.lower() == 'e'):
            counterTrue+=1
        if (letter.lower() == 'l'):
            counterLove+=1
        if (letter.lower() == 'o'):
            counterLove+=1
        if (letter.lower() == 'v'):
            counterLove+=1
        if (letter.lower() == 'e'):
            counterLove+=1
    counterTrueLove =int(f"{counterTrue}{counterLove}") 
    if (counterTrueLove < 10 or counterTrueLove > 90):
        return f"Your score is {counterTrueLove}, you go together like coke and mentos."
    if (counterTrueLove > 40 and counterTrueLove < 50):
        return f"Your score is {counterTrueLove}, you are alright together."
    else:
        return f"Your score is {counterTrueLove}."
            
print(trueLove(name1,name2))