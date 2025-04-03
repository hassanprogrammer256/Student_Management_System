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
        AuthText = 'LOGIN'
    #   -----AUTH LABELFRAME_____
        Auth_LabelFrame = LabelFrame(window,bg=WHITE,width=WINDOW_WIDTH,height =WINDOW_HEIGHT)
        Auth_LabelFrame.place(x=0,y=0)
        WelcomeBanner = Banner(window,color=GREEN_PRIMARY,width=WINDOW_WIDTH,height = (WINDOW_HEIGHT // 35),x=0,y=0,hovercolor=GREEN_SECONDARY)
        WelcomeBanner.draw()
        # -----AUTH FORM_____
        Form_LabelFrame = LabelFrame(window,bg=WHITE,width=500,height=650,border=1)
        Form_LabelFrame.place(x=500,y=100)
        Header_labelFrame = LabelFrame(Form_LabelFrame,bg=WHITE,width=500,height=100,border=0)
        Header_labelFrame.place(x=0,y=0)
        # ----Photo Icon____
        try:
            photo_icon = Image.open(IMAGE_ICON_PATH)
            resized_icon = photo_icon.resize((100,100))
            final_icon =ImageTk.PhotoImage(resized_icon)
            photo_icon_lbl = Label(Header_labelFrame, image=final_icon,border=0,bg=WHITE)
            photo_icon_lbl.image = final_icon
            photo_icon_lbl.place(x=5,y=2)
        except Exception as e:
            print(f"Error opening icon: {e}")
            photo_icon_lbl = Label(Header_labelFrame, text="Error: Unable to load icon", fg=RED, font=("Arial", 14))

        Auth_Text_lbl = Label(Header_labelFrame,text=AuthText,font=("Algerian",25),bg=WHITE,fg=BLACK)
        Auth_Text_lbl.place(x=100,y=40)
        