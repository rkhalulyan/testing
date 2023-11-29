import tkinter as tk
import registration
import login

def setup_main_gui():
    window = tk.Tk()
    window.title("Online Store User System")

    tk.Label(window, text="Welcome to the Online Store User System").pack(pady=10)

    registration_button = tk.Button(window, text="User Registration", command=registration.setup_gui)
    registration_button.pack(pady=5)

    login_button = tk.Button(window, text="User Login", command=login.setup_login_gui)
    login_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    setup_main_gui()
