from config import *
from constants import *
from banner import Banner

class Authenticate:
    def __init__(self,window):
        self.window = window
        self.username = StringVar()
        self.password = StringVar()
        self.username_entry = Entry(self.window, textvariable=self.username)
        self.password_entry = Entry(self.window, textvariable=self.password, show="*")
        self.login_button = Button(self.window, text="Login", command=self.login)

        self.draw()

    def draw(window):
    #   -----AUTH LABELFRAME_____
        Auth_LabelFrame = LabelFrame(window,bg=WHITE,width=WINDOW_WIDTH,height =WINDOW_HEIGHT)
        Auth_LabelFrame.place(x=0,y=0)
        WelcomeBanner = Banner(window,color=GREEN_PRIMARY,width=WINDOW_WIDTH,height = (WINDOW_HEIGHT // 35),x=0,y=0,hovercolor=GREEN_SECONDARY)
        WelcomeBanner.draw()
        # -----AUTH FORM_____
        Form_LabelFrame = LabelFrame(window,bg=WHITE,width=500,height=650,border=1)
        Form_LabelFrame.place(x=500,y=100)
        
        # ----Photo Icon____
        photo_icon = Image.open(IMAGE_ICON_PATH)
        resized_icon = photo_icon.resize((100, 100))
        final_icon =ImageTk.PhotoImage(resized_icon)
        photo_icon_lbl = Label(Form_LabelFrame, image=final_icon)
        photo_icon_lbl.place(x=70,y=20)
  