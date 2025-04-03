from constants import *

class StudentManagementApp:
    def __init__(self, root, system):
        self.system = system
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        root.resizable(False, False) 
        root.config(bg=WHITE)
        root.title("Student Management System")
        Authenticate.draw(root)

if __name__ == "__main__":
    root = tk.Tk()
    system = StudentManagementSystem()
    app = StudentManagementApp(root, system)
    root.mainloop()