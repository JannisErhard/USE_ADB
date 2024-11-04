import tkinter as tk
import string
import os

def key(i):
    print(i.char)
    if i.char == '?':
        os.system(f"adb shell input text \\\\{i.char}")
    else:
        os.system(f"adb shell input text {i.char}")

def delete(i):
    os.system("adb shell input keyevent 67")

def space(i):
    os.system("adb shell input keyevent 62")

def left(i):
    os.system("adb shell input keyevent 21")

def right(i):
    os.system("adb shell input keyevent 22")

def up(i):
    os.system("adb shell input keyevent 19")

def down(i):
    os.system("adb shell input keyevent 20")

def enter(i):
    os.system("adb shell input keyevent 66")

def home(i):
    os.system("adb shell input keyevent 3")

def recent(i):
    os.system("adb shell input keyevent KEYCODE_APP_SWITCH")


root = tk.Tk()

for letter in list(string.ascii_lowercase):
    root.bind(letter, key)
for letter in list(string.ascii_uppercase):
    root.bind(letter, key)

root.bind('.', key)
root.bind(',', key)
root.bind(':', key)
root.bind('?', key)
root.bind('!', key)
root.bind('<BackSpace>', delete)
root.bind('<space>', space)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Return>', enter)
root.bind('<Escape>', home)
root.bind('<Tab>', recent)

tk.mainloop()

# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
# https://gist.github.com/arjunv/2bbcca9a1a1c127749f8dcb6d36fb0bc
# https://stackoverflow.com/questions/33898029/adb-how-to-tap-close-from-recent-apps-to-completely-through-adb-one-liner-comma
