def chatbot_template():
    print("Welcome! I'm your friendly chatbot.")
    
    user_name = input("What's your name? ")
    user_age = input("How old are you? ")

    print(f"Hello {user_name}! How can I assist you today?")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Placeholder Option 1")
        print("2. Placeholder Option 2")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")
#d
        if choice == "1":
            print("You selected Placeholder Option 1.")
        elif choice == "2":
            print("You selected Placeholder Option 2.")
        elif choice == "3":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    chatbot_template()
