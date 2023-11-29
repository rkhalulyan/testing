import tkinter as tk
from tkinter import messagebox
import db_connection

def register_user(username, password, confirm_password, firstName, lastName, email):
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    conn = db_connection.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user (username, password, firstName, lastName, email) VALUES (%s, %s, %s, %s, %s)",
                       (username, password, firstName, lastName, email))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        cursor.close()
        conn.close()

def setup_gui():
    window = tk.Tk()
    window.title("User Registration")

    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Label(window, text="Confirm Password").pack()
    confirm_password_entry = tk.Entry(window, show="*")
    confirm_password_entry.pack()

    tk.Label(window, text="First Name").pack()
    first_name_entry = tk.Entry(window)
    first_name_entry.pack()

    tk.Label(window, text="Last Name").pack()
    last_name_entry = tk.Entry(window)
    last_name_entry.pack()

    tk.Label(window, text="Email").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    register_button = tk.Button(window, text="Register", 
                                command=lambda: register_user(username_entry.get(),
                                                              password_entry.get(),
                                                              confirm_password_entry.get(),
                                                              first_name_entry.get(),
                                                              last_name_entry.get(),
                                                              email_entry.get()))
    register_button.pack()

    window.mainloop()