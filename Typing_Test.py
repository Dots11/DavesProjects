import curses
from curses import wrapper
import time
import random

import seconds as seconds


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPress any key to begin!") #1,0 or \n
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0): # these are parameters
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")

    for i, char in enumerate(current):  # loop through these keys, with characters placed on the screen
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip() #randomly choose one element from the list of stringed text; - 'strip' removes the \n from each line


def wpm_test(stdscr):
    target_text = "Hello world this some test text for this app!" # or load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True) #do not delay  waiting a user to hit a key

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()  # if disabled, it will repeat the text multiple times!!!
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break # brings us outside this while loop



        try:
            key = stdscr.getkey() #list of keys user pressed # crash when user does not type anything
        except:
            continue # if crashes, the 'except' statement brings us back to the top of the while loop

        if ord(key) == 27: # numeric representation of key on keyboard e.g "a" = 97. "27" is escape
            break

        if key in ("KEY_BACKSPACE", '\b', '\x7f'): # latter 2 refer to backspace key, representation of different systems e.g. Windows and Mac.
            if len(current_text) > 0:
                current_text.pop() # gets rid of last element from current list/ text via Backspace
        elif len(current_text) < len(target_text): # so not to add backspace key to our current text, just want to remove the current character
            current_text.append(key)


def main(stdscr): # when this function is run, colours initialised and  start screen called.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True: # play this code many times as possible
        wpm_test(stdscr) # call this function and good to go
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)

