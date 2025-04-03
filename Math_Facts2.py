import streamlit as st
import random

# Function to ask a question and validate the answer
def ask_question(level):
    if level == 1:
        num1 = random.randint(0, 5)
        num2 = random.randint(0, 5)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    elif level == 2:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    elif level == 3:
        num1 = random.randint(10, 12)
        num2 = random.randint(0, 5)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    elif level == 4:
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    elif level == 5:
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        question = f"What’s {num1} + {num2}?"
        answer = num1 + num2
    
    # Show question and input box
    user_answer = st.text_input(question, "")
    
    return user_answer, answer

# Streamlit app layout
def main():
    st.title("Math Adventure Game!")
    st.write("Welcome to the Math Adventure! Let's practice your addition skills!")
    st.write("Answer 12 questions correctly to level up and become a Math Star!")
    
    # Session state to track user progress
    if "level" not in st.session_state:
        st.session_state.level = 1
        st.session_state.correct_answers = 0
    
    level = st.session_state.level
    correct_answers = st.session_state.correct_answers
    
    # Ask question based on the selected level
    user_answer, answer = ask_question(level)
    
    # Check if answer is correct
    if user_answer:
        if int(user_answer) == answer:
            st.success("Great job! You're on the right track!")
            st.session_state.correct_answers += 1
        else:
            st.error(f"Oops! The correct answer was {answer}.")
    
    # When the player answers 12 questions correctly, level up
    if st.session_state.correct_answers >= 12:
        if level < 5:
            st.session_state.level += 1
            st.session_state.correct_answers = 0
            st.balloons()
            st.success(f"Awesome! You've advanced to Level {level + 1}!")
        else:
            st.session_state.level = 5
            st.session_state.correct_answers = 0
            st.balloons()
            st.success("Congratulations! You’ve completed all levels and became a Math Star!")
    
    # Show current level and number of correct answers
    st.write(f"Level {level}: Answer {12 - correct_answers} more questions correctly to level up!")
    
    # Provide an option to restart the game
    if st.button("Restart Game"):
        st.session_state.level = 1
        st.session_state.correct_answers = 0
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    main()

