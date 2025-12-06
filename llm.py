import google.generativeai as genai

# Configure your API Key directly
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

chat_history = []  # Stores conversation


def generate_response(user_input):
    global chat_history

    # Add user message
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # Send full chat history
    response = model.generate_content(chat_history)

    bot_reply = response.text

    # Add bot reply (role MUST BE 'model')
    chat_history.append({
        "role": "model",
        "parts": [{"text": bot_reply}]
    })

    return bot_reply


def main():
    print("\n🤖 Gemini Chat Started — type 'exit' to stop\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat Ended!")
            break

        answer = generate_response(user_input)
        print("Gemini:", answer)


if __name__ == "__main__":
    main()

