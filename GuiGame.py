import tkinter as tk
import random

root=tk.Tk()
root.geometry("500x150")

attempts = 10
answer = random.randint(1,10)

def check_answer():
    global attempts
    global text
    
    attempts -=1
    
    guess= int(entry_window.get())
    
    if answer == guess:
        text.set("You Won!!! Congrats")
        btn_check.pack_forget()
    elif attempts == 0:
        text.set("you are out of attempts")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have  "+ str(attempts)+ " attempts remaining, Go Higher!!")
    elif guess > answer:
        text.set("Incorrect! You have  "+ str(attempts)+ " attempts remaining, Go Lower!!")
    return

Title=tk.Label(root, text="Guess the number between 1 and 10")
Title.pack()

entry_window=tk.Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check=tk.Button(root, text='Check', command=check_answer)
btn_check.pack()

btn_quit=tk.Button(root, text='Quit', command=root.destroy)
btn_quit.pack()

text = tk.StringVar()
text.set("You have 10 attempts remaining! Good Luck!")

guess_attempts= tk.Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()