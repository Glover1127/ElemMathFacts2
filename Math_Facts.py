import streamlit as st
import random

# Function to display questions and give feedback
def ask_question(level):
    if level == 1:
        # Level 1: Numbers between 0 and 5
        num1 = random.randint(0, 5)
        num2 = random.randint(0, 5)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    elif level == 2:
        # Level 2: Numbers between 0 and 10
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        question = f"A frog jumps {num1} steps, then {num2} more. How far did it go?"
        answer = num1 + num2
    elif level == 3:
        # Level 3: Numbers where one number is between 10 and 12
        num1 = random.randint(10, 12)
        num2 = random.randint(0, 5)
        question = f"You have {num1} candies, and your friend gives you {num2} more. How many now?"
        answer = num1 + num2
    elif level == 4:
        # Level 4: Any numbers from 0 to 12
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        question = f"A tree has {num1} apples, and {num2} more grow. How many apples total?"
        answer = num1 + num2
    elif level == 5:
        # Level 5: Sums up to 24
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        question = f"A rocket flies {num1} miles, then {num2} more. How far did it travel?"
        answer = num1 + num2
    
    # Show question and input box
    user_answer = st.text_input(question, "")
    
    # Check if answer is correct
    if user_answer:
        if int(user_answer) == answer:
            st.success("Great job! You're a math star!")
            return True
        else:
            st.error(f"Oops! The correct answer was {answer}.")
            return False
    return False

# Streamlit app layout
def main():
    st.title("Math Adventure Game!")
    st.write("Welcome to the Math Adventure! Let's practice your addition skills!")
    st.write("Complete all 5 levels to become a Math Star!")
    
    # Define the level system
    level = st.slider("Select Your Level", 1, 5, 1)
    
    # Ask question based on the selected level
    if ask_question(level):
        st.balloons()
    
    # Progress message
    st.write(f"Level {level}: Keep going, you're doing great!")

# Run the app
if __name__ == "__main__":
    main()
