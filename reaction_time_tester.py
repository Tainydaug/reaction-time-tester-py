import tkinter as tk
import random
import time

start = 0
best = 0
waiting = False
ready = False
after_id = None

def reset(msg):
    global waiting, ready
    waiting = False
    ready = False
    box.config(bg="gray")
    label.config(text=msg)
    button.config(state="normal")

def turn_green():
    global waiting, ready, start
    box.config(bg="green")
    label.config(text="click now!")
    waiting = False
    ready = True
    start = time.perf_counter()      # start timer

def start_game():
    global waiting, ready, after_id
    button.config(state="disabled")
    result.config(text="")
    box.config(bg="red")
    label.config(text="wait for green...")
    waiting = True
    ready = False
    delay = random.randint(1000, 4000)      # random delay
    after_id = root.after(delay, turn_green)

def click(event):
    global best
    if ready:
        t = int((time.perf_counter() - start) * 1000)      # stop timer
        result.config(text=str(t) + " ms")
        if best == 0 or t < best:
            best = t
            bestlabel.config(text="best: " + str(best) + " ms")
        reset("press start to try again")
    elif waiting:
        root.after_cancel(after_id)      # cancel green
        result.config(text="too early!")
        reset("you clicked too early")

root = tk.Tk()
root.title("Reaction Time Tester")
root.geometry("400x350")

label = tk.Label(root, text="press start, wait for green", font=("Arial", 13))
label.pack(pady=15)

box = tk.Label(root, bg="gray", width=30, height=7)
box.pack(pady=10)
box.bind("<Button-1>", click)      # click event

result = tk.Label(root, text="", font=("Arial", 14, "bold"))
result.pack()

bestlabel = tk.Label(root, text="best: --")
bestlabel.pack()

button = tk.Button(root, text="Start", command=start_game)
button.pack(pady=10)

root.mainloop()
