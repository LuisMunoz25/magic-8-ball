import random # Import random to use randint and generate random numbers

# Variables used in our Magic 8-Ball
name = input("Enter your name: ")
user_name = " asks: "
question = input("Enter your question: ")
answer = ""

# Print a random number between 1(inclusive) to 9(inclusive) and save it in a variable called "random_number":
random_number = random.randint(1, 9)
# print(random_number)

# Use if/elif/else to pick random answers that were already assigned to a number from 1 to 9:
if random_number == 1:
   answer = "Yes - definitely"
elif random_number == 2:
   answer = "It is decidedly so"
elif random_number == 3:
   answer = "Without a doubt"
elif random_number == 4:
   answer = "Reply hazy, try again"
elif random_number == 5:
   answer = "Ask again later"
elif random_number == 6:
   answer = "Better not tell you now"
elif random_number == 7:
   answer = "My sources say no"
elif random_number == 8:
   answer = "Outlook not so good"
elif random_number == 9:
   answer = "Very doubtful"
else:
   answer = "Error"

# Use "match statement" as an alternative of if/else/else to pick random answers that were already assigned to a number from 1 to 9::
# match random_number:
#   case 1:
#     answer = "Yes - definitely"
#   case 2:
#     answer = "It is decidedly so"
#   case 3:
#     answer = "Without a doubt"
#   case 4:
#     answer = "Reply hazy, try again"
#   case 5:
#     answer = "Ask again later"
#   case 6:
#     answer = "Better not tell you now"
#   case 7:
#     answer = "My sources say no"
#   case 8:
#    answer = "Outlook not so good"
#   case 9:
#     answer = "Very doubtful"
#   case default:
#     answer = "Error"
    
# Use if/elif/else to print answers based on the conditions given below:
if name == "" and question == "":
  question = "Enter your question first, please!"
  answer = ""
elif question == "":
  question = "Enter your question first, please!"
  answer = ""
  name = ""
elif name == "":
  name = "Question: "
else:
  name = name + user_name

question = print(name + question)
answer = print("Magic 8 Ball's answer: " + answer)

