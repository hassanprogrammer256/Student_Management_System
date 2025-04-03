from config import *
from constants import *

class Entry(Entry):
    def __init__(self,placeholder, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        
        # Set up placeholder behavior
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_focus_out)
        
        # Initially set the placeholder
        self.insert(0, self.placeholder)
        self.bind("<Button-1>", self.remove_placeholder)
        self.bind("<Key>", self.remove_placeholder)

    def on_focus(self, event):
        if self.get() == self.placeholder:
           self.delete(0, END)

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)

    def remove_placeholder(self, event):
        
        if self.get() == self.placeholder:
            self.delete(0, tk.END)