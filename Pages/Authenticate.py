import os
import sys

# Get the path of the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Append the project root to sys.path
sys.path.append(PROJECT_ROOT)

from constants import *
class Authenticate:
    def __init__(self,window):
        self.window = window
        # self.username = StringVar()
        # self.password = StringVar()
        # self.username_entry = Entry(self.window, textvariable=self.username)
        # self.password_entry = Entry(self.window, textvariable=self.password, show="*")
        # self.login_button = Button(self.window, text="Login", command=self.login)

        self.draw()

    def draw(window):
        print("drawing")

  