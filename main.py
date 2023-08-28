import json

trooms = {}
with open("teacher list.json", 'r') as jsonf:
  trooms = json.load(jsonf)
teachers = list(trooms)


def checkInput(inputType):
  
  if int(inputType) == 1:
    q2 = input("Which teacher do you want to find? ")
    for i in q2.split():
      if i in teachers:
        print(trooms[i])
      else:
        pass
  elif int(inputType) == 2:
		awesomeInput = input('Which letter building do you need the location of? Use the format "Q Building"')
		if "R" in awesomeInput:
			
  elif int(inputType) == 3:
    for teacher in list(trooms):
      if trooms[teacher][0] == q2.lower():
        print(teacher)


print(
    "Hi, this chatbot is designed to help you learn about the locations on campus! \n"
)
userInput = ""
while True:
  # print("Ask me a question about a building on campus!")
  print("Type the number of the type of question you would like to ask.\n")
  print("1. Which room a teacher is in.")
  print("2. Where a building is.")
  print("3. What teachers are in a building.")
  userInput = input(
      "Type the number. Type 'q' to quit, or type 'h' for help. \n")
  if (userInput == "h"):
    print(
        "If the chatbot can't answer one of your questions, you can probably find the answer on the Amador website: https://amador.pleasantonusd.net/"
    )
  if userInput == "q":
    print("Goodbye")
    break
  try:
    checkInput(int(userInput))
  except:
    continue
  print("\n")
print("Goodbye!")
