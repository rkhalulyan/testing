import tkinter as tk
from tkinter import messagebox
import db_connection

def login_user(username, password):
    conn = db_connection.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or password")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        cursor.close()
        conn.close()

def setup_login_gui():
    window = tk.Tk()
    window.title("User Login")

    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    login_button = tk.Button(window, text="Login", 
                             command=lambda: login_user(username_entry.get(),
                                                        password_entry.get()))
    login_button.pack()

    window.mainloop()
