import curses
import time import sys from curses.textpad import Textbox, rectangle from ed import ed  file_to_edit = sys.argv[1] buffer = ed.Buffer(file_name=file_to_edit)  def command(stdscr, repl_y, repl_x):     stdscr.addstr(repl_y, 0, ":")     editwin = curses.newwin(1, repl_x - 1, repl_y, repl_x + 2)     stdscr.refresh()     box = Textbox(editwin)     box.edit()     return box.gather()  def handle_cmd(ed_cmd):     if ed_cmd == "q":         sys.exit(0)
    else:
        ed.process(ed_cmd, buffer)

def main(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    win_y = max_y - 3
    win_x = max_x - 1
    status_y = win_y + 1
    status_x = win_x
    repl_y = status_y + 1
    repl_x = status_x

    pad = curses.newpad(len(buffer.lines) + 1, 100)
    stdscr.addstr(status_y, 0, file_to_edit, curses.A_REVERSE)

    for i, line in enumerate(buffer.lines):
        pad.addstr(i, 0, line)

    cur_y = 0
    pad.refresh(cur_y,0, 0,0, win_y, win_x)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()

        if key == " " or key == "KEY_DOWN":
            if cur_y < len(buffer.lines):
                cur_y += 1
        elif key == "KEY_UP":
            if cur_y > 0:
                cur_y -= 1
        elif key == "q":
            sys.exit(2)
        elif key == ":":
            ed_cmd = command(stdscr, repl_y, repl_x)
            handle_cmd(ed_cmd.strip())
            pad.clear()
            for i, line in enumerate(buffer.lines):
                pad.addstr(i, 0, line)
        else:
            curses.flash()

        pad.refresh(cur_y,0, 0,0, win_y, win_x)

curses.wrapper(main)
