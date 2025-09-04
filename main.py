import tkinter as tk
import random
from tkinter import messagebox, ttk
import json
import os
import time

class Stats:
    def __init__(self, filepath='game_stats_ngg.json'):
        self.filepath = filepath

        self.stats = {
            'games_played': 0,
            'games_won': 0,
            'total_attempts': 0,
            'best_game': None
        }

        self.load_stats()

    def load_stats(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.stats = json.load(f)

    def save_stats(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.stats, f)

    def update_stats(self, won, attempts):
        self.stats['games_played'] += 1

        if won:
            self.stats['games_won'] += 1

            if self.stats['best_game'] is None or attempts < self.stats['best_game']:
                self.stats['best_game'] = attempts

        self.stats['total_attempts'] += attempts
        self.save_stats()

    def get_stats(self):
        return self.stats

stats = Stats()

win = tk.Tk()
win.title("Main Menu")
win.configure(bg = '#0D1117')

style = ttk.Style()
style.theme_use('clam')
style.configure("Neon.TFrame", bg = '#0D1117', fg = '#C9D1D9', font = ('Arial', 12))

wn = tk.Frame(win, bg = '#0D1117')
wn.pack(fill = 'x', pady = 20)

lbl = tk.Label(wn, text = "NUMBER GUESSING GAME", font = ("Helvetica", 32), fg = "green", bg = '#0D1117')
lbl.pack(pady = 20)

btn = tk.Button(wn, text = "Start Game", font = ("Helvetica", 14), bg = '#238636', fg = 'white')
btn.pack(pady = 20)

def setup_game(attempts, win2):
    win2.destroy()
    num = random.randint(1, 100)
    nr = attempts

    win3 = tk.Toplevel(win)
    win3.title("Guess the Number")
    win3.configure(bg = '#0D1117')

    wn2 = tk.Frame(win3, bg = '#0D1117')
    wn2.pack(fill = 'x', pady = 20)

    lbl2 = tk.Label(wn2, text = f"You have {attempts} attempts to guess the number between 1 and 100", font = ("Helvetica", 14), fg = "orange", bg = '#0D1117')
    lbl2.pack(pady = 20)

    ipt = tk.Entry(wn2, font = ("Helvetica", 14))
    ipt.pack(pady = 15)

    def check():
        nonlocal attempts

        try:
            guess = int(ipt.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.", parent = win3)
            return

        if guess < 1 or guess > 100:
            messagebox.showwarning("Out of Bounds", "Please guess a number between 1 and 100.", parent = win3)
            return

        attempts -= 1

        if guess < num:
            messagebox.showinfo("Try Again", "Too low!", parent = win3)
        elif guess > num:
            messagebox.showinfo("Try Again", "Too high!", parent = win3)
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {num} correctly!", parent = win3)
            stats.update_stats(True, (nr - attempts))
            win3.destroy()
            return

        if attempts == 0:
            messagebox.showinfo("Game Over", f"You've run out of attempts! The number was {num}.", parent = win3)
            stats.update_stats(False, nr)
            win3.destroy()
            return
        else:
            lbl2.config(text = f"You have {attempts} attempts left. Try again!")

        ipt.delete(0, tk.END)

    def if_enter(event):
        check()

    ipt.bind("<Return>", if_enter)

    btn2 = tk.Button(wn2, text = "Submit Guess", font = ("Helvetica", 14), bg = '#238636', fg = 'white', command = check)
    btn2.pack(pady = 10)

    win3.geometry("800x600")

def start_game():
    win2 = tk.Toplevel(win)
    win2.title("Select Difficulty")
    win2.configure(bg = '#0D1117')

    wn2 = tk.Frame(win2, bg = '#0D1117')
    wn2.pack(fill = 'x', pady = 20)

    lbl2 = tk.Label(wn2, text = "Select Difficulty Level", font = ("Helvetica", 24), fg = "orange", bg = '#0D1117')
    lbl2.pack(pady = 20)

    btn1 = tk.Button(wn2, text = "Easy (10 attempts)", font = ("Helvetica", 14), bg = '#238636', fg = 'white', command = lambda: setup_game(10, win2))
    btn1.pack(pady = 10)

    btn2 = tk.Button(wn2, text = "Medium (7 attempts)", font = ("Helvetica", 14), bg = '#FB8500', fg = 'white', command = lambda: setup_game(7, win2))
    btn2.pack(pady = 10)

    btn3 = tk.Button(wn2, text = "Hard (5 attempts)", font = ("Helvetica", 14), bg = '#DA3633', fg = 'white', command = lambda: setup_game(5, win2))
    btn3.pack(pady = 10)

    win2.geometry("400x300")

btn.config(command = start_game)

btn1 = tk.Button(wn, text = "View Stats", font = ("Helvetica", 14), bg = '#238636', fg = 'white')

def view_stats():
    data = stats.get_stats()

    stats_msg = (
        f"Games Played: {data['games_played']}\n"
        f"Games Won: {data['games_won']}\n"
        f"Total Attempts: {data['total_attempts']}\n"
        f"Best Game (fewest attempts): {data['best_game'] if data['best_game'] is not None else 'N/A'}"
    )

    messagebox.showinfo("Game Statistics", stats_msg)

btn1.config(command = view_stats)
btn1.pack(pady = 20)

def quit_app():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        win.destroy()

btn2 = tk.Button(wn, text = "Quit", font = ("Helvetica", 14), bg = '#7D0A0A', fg = 'white', command = quit_app)
btn2.pack(pady = 20)

win.geometry("800x600")
win.mainloop()