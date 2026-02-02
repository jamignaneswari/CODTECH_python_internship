# Task 3: AI Chatbot with NLP
# CODTECH Python Internship
# Intern Name: Jami Gnaneswari

print("🤖 AI Chatbot with NLP is running")
print("Type 'bye' to exit\n")

# Basic NLP preprocessing (tokenization)
def preprocess(text):
    text = text.lower()
    tokens = text.split()
    return tokens

def chatbot_response(user_input):
    tokens = preprocess(user_input)

    if "hello" in tokens or "hi" in tokens:
        return "Hello! How can I help you?"

    elif "name" in tokens:
        return "I am an AI Chatbot built using NLP for the CODTECH Internship."

    elif "internship" in tokens:
        return "This Python internship focuses on real-time practical tasks."

    elif "codtech" in tokens:
        return "CODTECH provides internships to build real-world technical skills."

    else:
        return "Sorry, I didn't understand that. Please try again."

# Chat loop
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Chatbot: Goodbye! 👋")
        break
    print("Chatbot:", chatbot_response(user))