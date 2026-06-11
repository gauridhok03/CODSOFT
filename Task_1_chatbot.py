import datetime
import random
import string

# -----------------------------
# NOVA AI ASSISTANT
# -----------------------------

user_name = ""
command_count = 0

motivational_quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Believe in yourself and all that you are.",
    "Discipline is the bridge between goals and accomplishment.",
]

productivity_tips = [
    "Prioritize your most important task first.",
    "Avoid multitasking and focus on one task at a time.",
    "Take short breaks to maintain productivity.",
    "Plan your day before starting work."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer cold? It left its Windows open.",
    "Why do Python programmers wear glasses? Because they can't C.",
    "What is a computer's favorite snack? Microchips."
]


def show_help():
    print("\n========== AVAILABLE COMMANDS ==========")
    print("hello")
    print("my name is <name>")
    print("what is my name")
    print("what can you do")
    print("date")
    print("time")
    print("python")
    print("ai")
    print("machine learning")
    print("data science")
    print("calculator")
    print("motivate me")
    print("productivity tip")
    print("joke")
    print("commands used")
    print("help")
    print("exit")
   

def calculator():
    try:
        print("\nCalculator Operations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose operation (1-4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result =", num1 / num2)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")




print("=" * 55)
print("         NOVA AI ASSISTANT")
print(" A Rule-Based Virtual Personal Assistant")
print(" Type 'help' to view available commands")
print("=" * 55)

while True:

    user_input = input("\nYou: ").lower().strip()
    command_count += 1

    # Greetings
    if user_input in ["hello", "hi", "hey"]:

        if user_name:
            print(f"Nova: Hello {user_name}! How can I assist you today?")
        else:
            print("Nova: Hello! Welcome to Nova AI Assistant.")

    # Save name
    elif "my name is" in user_input:

        user_name = user_input.replace("my name is", "").strip().title()

        if user_name:
            print(f"Nova: Nice to meet you, {user_name}!")

    # Recall name
    elif "what is my name" in user_input:

        if user_name:
            print(f"Nova: Your name is {user_name}.")
        else:
            print("Nova: I don't know your name yet.")

    # Features
    elif "what can you do" in user_input:

        print("""
Nova AI Assistant Features:

• Date and Time Information
• AI and Python Knowledge
• Machine Learning Information
• Data Science Information
• Calculator
• Productivity Tips
• Motivational Quotes
• Jokes
""")

    # Date
    elif user_input == "date":
        print("Nova:", datetime.date.today())

    # Time
    elif user_input == "time":
        print("Nova:", datetime.datetime.now().strftime("%H:%M:%S"))

    # Python
    elif "python" in user_input:
        print(
            "Nova: Python is a high-level programming language used in AI, Data Science, Web Development, and Automation."
        )

    # AI
    elif user_input == "ai" or "artificial intelligence" in user_input:
        print(
            "Nova: Artificial Intelligence enables machines to mimic human intelligence and decision-making."
        )

    # Machine Learning
    elif "machine learning" in user_input:
        print(
            "Nova: Machine Learning is a subset of AI that allows systems to learn from data."
        )

    # Data Science
    elif "data science" in user_input:
        print(
            "Nova: Data Science involves extracting meaningful insights from data using statistics and programming."
        )

    # Calculator
    elif "calculator" in user_input:
        calculator()

    # Motivation
    elif "motivate me" in user_input:
        print("Nova:", random.choice(motivational_quotes))

    # Productivity
    elif "productivity" in user_input:
        print("Nova:", random.choice(productivity_tips))

    # Joke
    elif "joke" in user_input:
        print("Nova:", random.choice(jokes))

    # Commands Used
    elif "commands used" in user_input:
        print(f"Nova: You have used {command_count} commands.")

    # Help
    elif "help" in user_input:
        show_help()

    # Thanks
    elif "thanks" in user_input or "thank you" in user_input:
        print("Nova: You're welcome!")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:

        if user_name:
            print(f"Nova: Goodbye {user_name}! Have a wonderful day.")
        else:
            print("Nova: Goodbye! Have a wonderful day.")

        break

    # Unknown Query
    else:
        print("Nova: Sorry, I don't understand that command.")
        print("Nova: Type 'help' to see available commands.")