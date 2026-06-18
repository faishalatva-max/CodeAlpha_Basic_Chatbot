def chatbot():
    print(" ChatBot Started")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I am fine. Thanks for asking!")

        elif user == "your name":
            print("Bot: I am a Python ChatBot.")

        elif user == "what can you do":
            print("Bot: I can answer basic questions.")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
