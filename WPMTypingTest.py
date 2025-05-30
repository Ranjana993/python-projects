import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test!")
    stdscr.addstr("\nPress any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    
    for i, char in enumerate(current):
        if i >= len(target):  # Prevent index error if current text is longer than target
            break
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "Hello World, this is some test text for this app!"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if len(current_text) == len(target_text):
            stdscr.nodelay(False)
            stdscr.addstr(2, 0, "You completed the text! Press any key to exit...")
            stdscr.getkey()
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:  # ESC key
            break
            
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)