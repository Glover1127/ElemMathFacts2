import streamlit as st
import random

# Function to generate a random problem for the level
def generate_problem(level):
    x = random.randint(0, 12)
    return f"{level} + {x}", level + x

# Function to display hints or encouragement messages
def display_hint(is_correct):
    if is_correct:
        return "Great job!"
    else:
        return "Oops! Try again. Remember, addition is combining numbers!"

# Initialize session state variables
def initialize_session_state():
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'level' not in st.session_state:
        st.session_state.level = 1
    if 'problem' not in st.session_state or 'correct_answer' not in st.session_state:
        problem, correct_answer = generate_problem(st.session_state.level)
        st.session_state.problem = problem
        st.session_state.correct_answer = correct_answer
    if 'message' not in st.session_state:
        st.session_state.message = ""
    if 'submission_count' not in st.session_state:
        st.session_state.submission_count = 0  # To ensure unique keys for text_input

# Main game logic
def game():
    st.title("Math Facts Game")
    st.write("Welcome to the Math Facts Game! Select your level and start solving!")

    # Initialize session state
    initialize_session_state()

    # Level selection (only shown at the start)
    if st.session_state.level == 1 and st.session_state.score == 0:
        selected_level = st.selectbox("Choose your starting level:", [i for i in range(1, 15)])
        st.session_state.level = selected_level
        st.session_state.problem, st.session_state.correct_answer = generate_problem(selected_level)

    # Display current level and problem
    st.write(f"Level {st.session_state.level}: Solve the problem:")
    st.write(f"What is {st.session_state.problem}?")

    # Progress bar
    progress = (st.session_state.score + 1) / 15
    st.progress(progress)

    # Use a form to handle Enter key submission
    with st.form(key=f"form_{st.session_state.level}_{st.session_state.score}_{st.session_state.submission_count}"):
        # Unique key for text_input that changes with each submission
        user_answer = st.text_input("Your answer:", value="", key=f"input_{st.session_state.level}_{st.session_state.score}_{st.session_state.submission_count}")
        submit_button = st.form_submit_button(label="Submit Answer")

        # Process submission when Enter is pressed or button is clicked
        if submit_button:
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == st.session_state.correct_answer:
                    st.session_state.score += 1
                    st.session_state.message = display_hint(True)
                else:
                    st.session_state.score -= 1
                    st.session_state.message = display_hint(False)

                # Check if score goes negative
                if st.session_state.score < 0:
                    st.session_state.message = "You lost this level. Try again!"
                    st.session_state.score = 0
                # Check if level is completed
                elif st.session_state.score >= 15:
                    st.session_state.message = f"Congratulations! You've completed Level {st.session_state.level}!"
                    st.session_state.level += 1
                    st.session_state.score = 0
                    if st.session_state.level > 14:
                        st.write("Congratulations! You've completed all levels!")
                        st.balloons()
                        st.stop()
                # Generate new problem for the next question
                st.session_state.problem, st.session_state.correct_answer = generate_problem(st.session_state.level)
            else:
                st.session_state.message = "Please enter a valid number."

            # Increment submission count to force a new text_input with a cleared value
            st.session_state.submission_count += 1

    # Display feedback message
    if st.session_state.message:
        st.write(st.session_state.message)

# Run the game
if __name__ == "__main__":
    game()