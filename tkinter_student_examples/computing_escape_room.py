# @Author - Federico

# Hello Ms. Camilleri, this was an unfinished code i had started in summer, but had bugs adn didn't run as intended, so I fixed it and added 2 of the 4 questions
# Anyways hope you enjoy it :)

import tkinter  # Import the tkinter GUI library

def question2(parent_window):
    # Close the previous window
    parent_window.destroy()

    # Create a new window for the second question
    window2 = tkinter.Tk()
    window2.title("Escape Room")
    window2.geometry("500x500")
    window2.resizable(False, False)

    # Create and position title labels
    app_title = tkinter.Label(window2, text="Colour Representation!", font=("Ariel", 20, "bold"), fg='black')
    app_title.pack(pady=20)

    q_2_title = tkinter.Label(window2, text="2. Hexadecimal Color Blending:", font=("Ariel", 15, "bold"), fg='black')
    q_2_title.pack(pady=20)
    
    # Create question label
    q_2 = tkinter.Label(window2, text="What is the resulting color when blending (averaging) \n#FF5733 (a red-orange) with #33FF57 (a green)? \nThe two colors are blended equally.", font=("Ariel", 15), fg='black')
    q_2.pack(pady=10)

    # Variable to store the selected radio button option
    selected_option2 = tkinter.StringVar(value="")
     
    def check_answer2():
        # Get the selected answer
        answer = selected_option2.get()
        
        # Handle different answer scenarios
        if answer == "":
            # No answer selected
            result_window = tkinter.Toplevel()
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)
           
            result_title = tkinter.Label(result_window, text="You did not select an answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)

        elif answer == "D. #66FF45":
            # Correct answer
            result_window = tkinter.Toplevel(window2)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="Well done, you selected the correct answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            # Move to next question
            go_back_button = tkinter.Button(result_window, text="Next Question",  command=lambda: question3(window2), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)
            
        else:
            # Incorrect answer
            result_window = tkinter.Toplevel(window2)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="You selected the wrong answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)

    # Create radio button options for the question
    option_a = tkinter.Radiobutton(window2, text="A. #66B3A5", variable=selected_option2, value="A. #66B3A5", font=("Ariel", 12), fg="black")
    option_a.pack(anchor="w", padx=20, pady=5)

    option_b = tkinter.Radiobutton(window2, text="B. #80FF45", variable=selected_option2, value="B. #80FF45", font=("Ariel", 12), fg="black")
    option_b.pack(anchor="w", padx=20, pady=5)

    option_c = tkinter.Radiobutton(window2, text="C. #66A3C2", variable=selected_option2, value="C. #66A3C2", font=("Ariel", 12), fg="black")
    option_c.pack(anchor="w", padx=20, pady=5)
    
    option_d = tkinter.Radiobutton(window2, text="D. #66FF45", variable=selected_option2, value="D. #66FF45", font=("Ariel", 12), fg="black")
    option_d.pack(anchor="w", padx=20, pady=5)

    # Create submit button
    submit_button = tkinter.Button(window2, text="Submit", command=check_answer2, font=("Ariel", 12, "bold"))
    submit_button.pack(pady=20)

def question3(parent_window):
    # Similar structure to question2 - closes previous window and creates new window for third question
    parent_window.destroy()

    window3 = tkinter.Tk()
    window3.title("Escape Room")
    window3.geometry("500x500")
    window3.resizable(False, False)

    # Create and position labels
    app_title = tkinter.Label(window3, text="Colour Representation!", font=("Ariel", 20, "bold"), fg='black')
    app_title.pack(pady=20)

    q_3_title = tkinter.Label(window3, text="3. Color Contrast Calculation:", font=("Ariel", 15, "bold"), fg='black')
    q_3_title.pack(pady=20)
   
    # Question label
    q_3 = tkinter.Label(window3, text="What is the contrast ratio between: \n #1A1A1A (very dark gray) \nand #F5F5F5 (very light gray)? \n(Round to two decimal places.)", font=("Ariel", 15), fg='black')
    q_3.pack(pady=10)

    # Variable to store selected option
    selected_option3 = tkinter.StringVar(value="")
     
    def check_answer3():
        # Get selected answer and handle different scenarios (similar to check_answer2)
        answer = selected_option3.get()
        if answer == "":
            # No answer selected
            result_window = tkinter.Toplevel()
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="You did not select an answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)

        elif answer == "B. 21.23":
            # Correct answer
            result_window = tkinter.Toplevel(window3)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="Well done, you selected the correct answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            # End the program
            end_button = tkinter.Button(result_window, text="Close Escape Room", command=end_program, font=("Ariel", 12, "bold"))
            end_button.pack(pady=10)
        else:
            # Incorrect answer
            result_window = tkinter.Toplevel(window3)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="You selected the wrong answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)
     
    # Create radio button options for the third question
    option_a = tkinter.Radiobutton(window3, text="A. 12.45", variable=selected_option3, value="A. 12.45", font=("Ariel", 12), fg="black")
    option_a.pack(anchor="w", padx=20, pady=5)

    option_b = tkinter.Radiobutton(window3, text="B. 21.23", variable=selected_option3, value="B. 21.23", font=("Ariel", 12), fg="black")
    option_b.pack(anchor="w", padx=20, pady=5)

    option_c = tkinter.Radiobutton(window3, text="C. 18.52", variable=selected_option3, value="C. 18.52", font=("Ariel", 12), fg="black")
    option_c.pack(anchor="w", padx=20, pady=5)

    option_d = tkinter.Radiobutton(window3, text="D. 14.78", variable=selected_option3, value="D. 14.78", font=("Ariel", 12), fg="black")
    option_d.pack(anchor="w", padx=20, pady=5)

    # Create submit button
    submit_button = tkinter.Button(window3, text="Submit", command=check_answer3, font=("Ariel", 12, "bold"))
    submit_button.pack(pady=20)

def tryAgain(result_window):
    # Close the result window when user wants to retry
    result_window.destroy()

def end_program():
    # Quit the entire application
    quit()

def create_first_window():
    # Create the initial window for the first question
    my_window = tkinter.Tk()
    my_window.title("Escape Room")
    my_window.geometry("500x500")
    my_window.resizable(False, False)

    # Create and position labels for the first question
    app_title = tkinter.Label(my_window, text="Colour Representation!", font=("Ariel", 20, "bold"), fg='black')
    app_title.pack(pady=20)

    q_1_title = tkinter.Label(my_window, text="1. Color Manipulation - RGB Adjustment:", font=("Ariel", 15, "bold"), fg='black')
    q_1_title.pack(pady=20)

    # Question label
    q_1 = tkinter.Label(my_window, text="Given the color #8A2BE2 (a shade of blue-violet), \nwhat is the result of darkening this color by 30% \n(i.e., reducing the RGB values by 30%)?", font=("Ariel", 15), fg='black')
    q_1.pack(pady=10)

    # Variable to store selected option
    selected_option1 = tkinter.StringVar(value="")

    def check_answer1():
        # Get selected answer and handle different scenarios
        answer = selected_option1.get()
        if answer == "":
            # No answer selected
            result_window = tkinter.Toplevel()
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="You did not select an answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)

        elif answer == "C. #602799":
            # Correct answer
            result_window = tkinter.Toplevel(my_window)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="Well done, you selected the correct answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            # Move to next question
            go_back_button = tkinter.Button(result_window, text="Next Question", command=lambda: question2(my_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)
        else:
            # Incorrect answer
            result_window = tkinter.Toplevel(my_window)
            result_window.title("Result")
            result_window.geometry("400x150")
            result_window.resizable(False, False)

            result_title = tkinter.Label(result_window, text="You selected the wrong answer!", font=("Ariel", 12, "italic"), fg="black")
            result_title.pack(pady=20)

            go_back_button = tkinter.Button(result_window, text="Retry", command=lambda: tryAgain(result_window), font=("Ariel", 12, "bold"))
            go_back_button.pack(pady=10)
            
    # Create radio button options for the first question
    option_a = tkinter.Radiobutton(my_window, text="A. #5C1A9A", variable=selected_option1, value="A. #5C1A9A", font=("Ariel", 12), fg="black")
    option_a.pack(anchor="w", padx=20, pady=5)

    option_b = tkinter.Radiobutton(my_window, text="B. #7A1C9F", variable=selected_option1, value="B. #7A1C9F", font=("Ariel", 12), fg="black")
    option_b.pack(anchor="w", padx=20, pady=5)

    option_c = tkinter.Radiobutton(my_window, text="C. #602799", variable=selected_option1, value="C. #602799", font=("Ariel", 12), fg="black")
    option_c.pack(anchor="w", padx=20, pady=5)

    option_d = tkinter.Radiobutton(my_window, text="D. #6F1EBD", variable=selected_option1, value="D. #6F1EBD", font=("Ariel", 12), fg="black")
    option_d.pack(anchor="w", padx=20, pady=5)

    # Create submit button
    submit_button = tkinter.Button(my_window, text="Submit", command=check_answer1, font=("Ariel", 12, "bold"))
    submit_button.pack(pady=20)

    # Start the main event loop
    my_window.mainloop()

# Start the application by creating the first window
create_first_window()
