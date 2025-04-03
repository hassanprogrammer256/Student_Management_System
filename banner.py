from constants import *
from config import *

class Banner:
    def __init__(self,root,width,height,x,y,color,hovercolor):
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.hovercolor = hovercolor
        self.height = height
        self.color = color
        self.banner = Label(self.root,width=self.width, height =self.height,bg=self.color)
        self.banner.config(cursor='hand2')
        # self.banner.bind("<Enter>", on_enter)
        # self.banner.bind("<Leave>", on_leave)
        
    def draw(self):
        self.banner.place(x=self.x, y=self.y)
        
    # def on_enter(e):
    #      e.widget['background'] = self.hovercolor 
    # def on_leave(e):
    #      e.widget['background'] = self.color
        