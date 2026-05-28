from datetime import datetime

print("=" * 50)
print("          SMART PYTHON CHATBOT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! I am SmartBot.")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You : ").lower()

    if user == "hello" or user == "hi":
        print("Bot : Hello! Hope you are doing well.")

    elif user == "how are you":
        print("Bot : I am absolutely fine!")

    elif user == "your name":
        print("Bot : My name is SmartBot.")

    elif user == "who created you":
        print("Bot : Vivek created me using Python.")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot : Current Time is", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's Date is", current_date)

    elif user == "joke":
        print("Bot : Why was the computer cold?")
        print("Bot : Because it forgot to close Windows!")

    elif user == "help":

        print("\nAvailable Commands:")
        print("----------------------")
        print("hello")
        print("how are you")
        print("your name")
        print("who created you")
        print("time")
        print("date")
        print("joke")
        print("bye\n")

    elif user == "bye":
        print("Bot : Goodbye! Have a great day.")
        break

    else:
        print("Bot : Sorry, I don't understand that.")