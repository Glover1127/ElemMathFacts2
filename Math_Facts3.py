import streamlit as st
import random
import time

# Function to generate a random problem for the level
def generate_problem(level):
    # Define the range of numbers for the level
    x = random.randint(0, 12)
    return f"{level} + {x}", level + x

# Function to display hints or encouragement messages
def display_hint(is_correct):
    if is_correct:
        return "Great job!"
    else:
        return "Oops! Try again. Remember, addition is combining numbers!"

# Main game logic
def game():
    st.title("Math Facts Game")
    st.write("Welcome to the Math Facts Game! Select your level and start solving!")

    # Level selection
    level = st.selectbox("Choose your starting level:", [i for i in range(1, 15)])

    # Initialize score and level progress
    score = 0
    level_progress = 0

    # Game loop for the selected level
    while level <= 14:
        st.session_state['score'] = score
        st.session_state['level'] = level
        problem, correct_answer = generate_problem(level)

        st.write(f"Level {level}: Solve the problem:")
        user_answer = st.text_input(f"What is {problem}?", key="answer_input")

        # Progress bar
        progress = (score + 1) / 15  # Progress bar based on score
        st.progress(progress)

        # Check if the user has entered an answer
        if st.button("Submit Answer"):
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    st.write(display_hint(True))
                else:
                    score -= 1
                    st.write(display_hint(False))
            else:
                st.write("Please enter a valid number.")
            
            # Reset input field after submission
            st.session_state.answer_input = ""

            # Check if score goes negative, restart the level
            if score < 0:
                st.write("You lost this level. Try again!")
                score = 0  # Reset score for the level
                continue

            # Check if player has completed the level (15 points)
            if score == 15:
                st.write(f"Congratulations! You've completed Level {level}!")
                level_progress += 1
                st.session_state['level'] += 1
                score = 0  # Reset score for the next level
                level += 1
                break

        # Game Over logic: If all levels are completed, show a message
        if level > 14:
            st.write("Congratulations! You've completed all levels!")
            st.balloons()
            st.stop()

# Run the game
if __name__ == "__main__":
    game()
