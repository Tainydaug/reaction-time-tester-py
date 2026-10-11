# Reaction Time Tester

A small desktop game written in Python with Tkinter that measures how fast you react. Press Start, wait for the box to turn green, and click it as quickly as you can. Your reaction time is shown in milliseconds.

<!-- Add a screenshot here after you run it, for example: ![screenshot](screenshot.png) -->

## How to play

1. Press **Start**. The box turns red.
2. Wait. After a random delay (1 to 4 seconds) the box turns green.
3. Click the box as fast as you can. Your time appears under the box.
4. Clicking while the box is still red shows "too early!" and cancels the round.
5. The best time of your session is shown at the bottom.

## Requirements

- Python 3 (Tkinter is included with the standard Windows and macOS installers)
- On Debian/Ubuntu/Kali, install Tkinter with `sudo apt install python3-tk`

No other libraries are needed.

## Run it

```
python reaction_time_tester.py
```

## How it works

- **Random delay:** `random.randint(1000, 4000)` picks a delay in milliseconds, so the green signal can't be predicted. `root.after()` schedules the box to turn green after that delay without freezing the window.
- **Timing:** when the box turns green, `time.perf_counter()` records the start time. On the click, the difference between now and the start time, multiplied by 1000, gives the reaction time in milliseconds.
- **Early clicks:** if you click during the red phase, `root.after_cancel()` stops the scheduled green change and the round ends.
- **State:** two flags, `waiting` (red phase) and `ready` (green phase), tell the click handler which case it is dealing with.
- **Events:** the box is a Label with a left-click handler attached through `bind("<Button-1>", click)`. `root.mainloop()` keeps the window running and listening for events.

## Concepts practiced

Tkinter widgets and layout, event handling, scheduling with `after()`, global state in functions, and measuring time with `perf_counter()`.

## Possible improvements

- Average of the last five attempts
- Saving the best score to a file
- A countdown or sound cue
- A cleaner structure using a class instead of global variables

## Notes

Practice project, written while learning Python GUI programming. Reaction time in this program also includes your screen and mouse delay, so treat the numbers as a fun comparison, not a precise measurement.

## Author

Tanishq Gyaneshwar Dhoke ([@Tainydaug](https://github.com/Tainydaug))
