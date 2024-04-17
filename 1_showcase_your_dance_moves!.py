#Task 1: Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") #added indentation to ensure proper program flow and remove errors
else:
    print("Take an umbrella!") #added indentation to ensure proper program flow and remove errors

#Task 2: Your Mood Today

current_mood = input("What is your current mood (happy or sad)?: ") #get current mood of the user

if current_mood == "happy": #test if they are happy first
    print("That's great to hear!")
else:
    if current_mood == "sad": #verify if they are sad instead
        print("I hope your day gets better!")
    else:
        print("I'm sorry, I don't understand that answer") #only shows if unknown moods/inputs are used 