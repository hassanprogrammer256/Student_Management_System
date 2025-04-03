from config import *
from constants import *
from banner import Banner
# from entry import Entry

class Authenticate:
    def __init__(self,window):
        self.window = window
        self.username = StringVar()
        self.password = StringVar()
        self.username_entry = Entry(self.window, textvariable=self.username)
        self.password_entry = Entry(self.window, textvariable=self.password, show="*")
        self.login_button = Button(self.window, text="Login", command=self.login)
    def draw(window,AuthText):
    #   -----AUTH LABEL FRAME_____
        Auth_LabelFrame = LabelFrame(window,bg=WHITE,width=WINDOW_WIDTH,height =WINDOW_HEIGHT)
        Auth_LabelFrame.place(x=0,y=0)
        WelcomeBanner = Banner(window,color=GREEN_PRIMARY,width=WINDOW_WIDTH,height = (WINDOW_HEIGHT // 35),x=0,y=0,hovercolor=GREEN_SECONDARY)
        WelcomeBanner.draw()
        # -----AUTH FORM_____
        Form_LabelFrame = LabelFrame(window,bg=WHITE,width=500,height=650,border=1)
        Form_LabelFrame.place(x=500,y=100)
        Header_labelFrame = LabelFrame(Form_LabelFrame,bg=WHITE,width=500,height=100,border=2)
        Header_labelFrame.place(x=0,y=0)
        FormDataLabelFrame = LabelFrame(Form_LabelFrame,bg=WHITE,width=500,height=600,border=0)
        FormDataLabelFrame.place(x=0,y=100)

        # ----Photo Icon-----
        try:
            photo_icon = Image.open(IMAGE_ICON_PATH)
            resized_icon = photo_icon.resize((95,95))
            final_icon =ImageTk.PhotoImage(resized_icon)
            photo_icon_lbl = Label(Header_labelFrame,image=final_icon,border=0,bg=WHITE,pady=4)
            photo_icon_lbl.image = final_icon
            photo_icon_lbl.place(x=5,y=1)
        except Exception as e:
            print(f"Error opening icon: {e}")
            photo_icon_lbl = Label(Header_labelFrame, text="Error: Unable to load icon", fg=RED, font=("Arial", 14))

        Auth_Text_lbl = Label(Header_labelFrame,text=AuthText.upper(),font=("Algerian",25),bg=WHITE,fg=BLACK)
        Auth_Text_lbl.place(x=100,y=40)
        
        # ----FORM DATA------------------------
        if AuthText.lower() == 'log in':
            LoginData = [
                {'title': 'username', 'placeholder': 'Enter Email or Reg.No'},
                {'title': 'password', 'placeholder': 'Enter Password'}
            ]
            
            for i, data in enumerate(LoginData):
 
                entry = Entry(FormDataLabelFrame, fg=GRAY_PRIMARY, font=("Arial", 14), width=40,
                            bd=1, highlightthickness=3, highlightbackground=GRAY_PRIMARY,
                            highlightcolor=GREEN_PRIMARY)
                entry.insert(0, data['placeholder'])  # Setting placeholder text
                entry.bind("<FocusIn>", lambda e, entry=entry: entry.delete(0, tk.END) if entry.get() == data['placeholder'] else None)
                entry.place(x=10, y=20 + (i * 50))

        else: 
            RegistrationData = [
                {'title': 'username', 'placeholder': 'Enter Username'},
                {'title': 'email', 'placeholder': 'Enter Email'},
                {'title': 'password', 'placeholder': 'Enter Password'},
                {'title': 'confirm password', 'placeholder': 'Confirm Password'}
            ]
            
            for i, data in enumerate(RegistrationData):
                label = Label(FormDataLabelFrame, text=data['title'], font=("Arial", 14), bg=WHITE, fg=BLACK)
                label.place(x=10, y=20 + (i * 90))  
                entry = Entry(FormDataLabelFrame, fg=GRAY_PRIMARY, font=("Arial", 15), width=30,
                            bd=1, highlightthickness=3, highlightbackground=GRAY_PRIMARY,
                            highlightcolor=GREEN_PRIMARY,placeholdr=data['placeholder'])
             
                entry.place(x=140, y=20 + (i * 90))
        
        
class Login(Authenticate):
    def __init__(self,window):
        super().__init__(window)
        
    def draw(window):
        Authenticate.draw(window, "Log in")
  
    
    
             
        
        