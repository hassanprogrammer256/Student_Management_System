# --------IMPORTS---------
import sys
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Specify the folder containing your classes
CLASSES_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'Classes')
PAGES_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'Pages')

# Append the Classes and Pages folders to the system path
sys.path.append(CLASSES_FOLDER_PATH)
sys.path.append(PAGES_FOLDER_PATH)

# Now you can import your required modules
from System import *
from Authenticate import *

# ---window initialization----
WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 800

# ------COLORS----------
WHITE = '#FFFFFF'
BLACK = '#000000'
GREEN_PRIMARY = '#009688'
GRAY_PRIMARY = '#495057'


