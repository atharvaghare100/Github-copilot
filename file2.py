"""Rock paper scissors game with a Tkinter GUI interface."""

import random
import tkinter as tk

options = ['rock', 'paper', 'scissors']



def get_computer_choice():
    return random.choice(options)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)


def quit_game():
    root.destroy()


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x220")
root.resizable(False, False)

header = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
header.pack(pady=12)

button_frame = tk.Frame(root)
button_frame.pack(pady=8)

for choice in options:
    button = tk.Button(
        button_frame,
        text=choice.capitalize(),
        width=10,
        command=lambda c=choice: play_round(c)
    )
    button.pack(side="left", padx=5)

computer_label = tk.Label(root, text="Computer choice will appear here.")
computer_label.pack(pady=8)

result_label = tk.Label(root, text="Choose rock, paper, or scissors.", font=("Arial", 12))
result_label.pack(pady=4)

quit_button = tk.Button(root, text="Quit", width=10, command=quit_game)
quit_button.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()