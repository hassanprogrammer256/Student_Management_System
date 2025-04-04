from config import *
from constants import *
from banner import Banner
from tkinter import font
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
        if AuthText.lower() == 'log in':
            form_height = 300
            formlabelframe_y_pos = 300
            ButtonText= 'Login'
            Action_x= 300
            ActionText= 'Register Now'
            formData_height= form_height-110
            promptingText= 'You Dont have an Account Yet?'
        else:
                form_height = 350
                formData_height= form_height-110
                formlabelframe_y_pos = 300
                Action_x =260
                ButtonText= 'Register'
                promptingText= 'Already have an Account ?'
                ActionText= 'LogIn Now'
                #   -----AUTH LABEL FRAME_____
        Auth_LabelFrame = LabelFrame(window,bg=WHITE,width=WINDOW_WIDTH,height =WINDOW_HEIGHT)
        Auth_LabelFrame.place(x=0,y=0)
        WelcomeBanner = Banner(window,color=GREEN_PRIMARY,width=WINDOW_WIDTH,height = (WINDOW_HEIGHT // 35),x=0,y=0,hovercolor=GREEN_SECONDARY)
        WelcomeBanner.draw()
        # -----AUTH FORM_____
        Form_LabelFrame = LabelFrame(window,bg=BLACK,width=500,height=form_height,border=5)
        Form_LabelFrame.place(x=500,y=formlabelframe_y_pos)
        Header_labelFrame = LabelFrame(Form_LabelFrame,bg=WHITE,width=490,height=100,border=2)
        Header_labelFrame.place(x=0,y=0)
        FormDataLabelFrame = LabelFrame(Form_LabelFrame,bg=WHITE,width=490,height=formData_height,border=0)
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
            ]
            
            for i, data in enumerate(RegistrationData):
                label = Label(FormDataLabelFrame, text=data['title'], font=("Arial", 14), bg=WHITE, fg=BLACK)
                label.place(x=10, y=20 + (i * 50))  
                entry = Entry(FormDataLabelFrame, fg=GRAY_PRIMARY, font=("Arial", 15), width=30,
                            bd=1, highlightthickness=3, highlightbackground=GRAY_PRIMARY,
                            highlightcolor=GREEN_PRIMARY)
                entry.insert(0, data['placeholder'])  # Setting placeholder text
                entry.bind("<FocusIn>", lambda e, entry=entry: entry.delete(0, tk.END) if entry.get() == data['placeholder'] else None)
             
                entry.place(x=140, y=20 + (i * 50))
                
                
        # ----LOGIN/REGISTER BUTTONS------------------------
        SubmissionBtn = Button(FormDataLabelFrame,text=ButtonText,bg=GREEN_PRIMARY,fg=WHITE,font=('Arial', 15), bd=0,cursor='hand2',width=30)
        SubmissionBtn.place(x=40, y=formData_height-65)
        
         # -------------HOVER EFFECTS-------------
        def on_submit_enter(event):
            SubmissionBtn['bg'] = '#218838'  # Darker green
      
          

        def on_submit_leave(event):
            SubmissionBtn['bg'] = GREEN_PRIMARY
            SubmissionBtn['fg'] = WHITE
           

# Bind hover events to the Submission button
        SubmissionBtn.bind("<Enter>", on_submit_enter)
        SubmissionBtn.bind("<Leave>", on_submit_leave)
        
        # ----OPTIONS----
        
        options_label = Label(FormDataLabelFrame, text=promptingText, font=("Arial", 12), fg=GREEN_SECONDARY,bg=WHITE)
        options_label.place(x=70, y=formData_height-24)
        action_btn = Label(FormDataLabelFrame, text=ButtonText, bg=WHITE, fg=BLACK, font=font.Font(underline=True),cursor='hand2', )
        action_btn.place(x=Action_x, y=formData_height-24)
        
        def on_action_enter(event):
    action_btn['bg'] = '#f0f0f0'  # Light gray background
    action_btn['fg'] = '#007bff'  # Change to blue
    action_btn['font'] = font.Font(underline=True, size=14)  # Increase font size

        def on_action_leave(event):
            action_btn['bg'] = WHITE
            action_btn['fg'] = BLACK
            action_btn['font'] = font.Font(underline=True)

# Bind hover events to the action button
        action_btn.bind("<Enter>", on_action_enter)
        action_btn.bind("<Leave>", on_action_leave)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
    
    
             
        
        