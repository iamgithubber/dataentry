from tkinter import *
from tkinter import messagebox  # Importing messagebox module from tkinter
from datetime import datetime   # Importing datetime module from datetime

def exit_application():
    """Function to exit the application."""
    main.destroy()  # Close the main window

def clear_data():
    """Function to clear data stored in the file."""
    with open('data', 'w') as file:  # Open file in write mode
        file.truncate(0)  # Clear the contents of the file
    messagebox.showinfo("Data Cleared", "Data has been cleared successfully.")  # Display a message box with information

def see_data():
    """Function to display the stored data."""
    see = Toplevel(main)  # Create a new window
    see.title('Database')  # Set the title of the new window
    with open('data', 'r') as file:  # Open file in read mode
        for data in file:  # Iterate through each line in the file
            Label(see, text=data, font='calibre 10 bold').pack()  # Create a label to display each line
    Button(see, text='Exit', command=see.destroy).pack()  # Create a button to close the new window

def enter_data():
    """Function to enter data into the file."""
    name1 = name.get()  # Get the value from the name entry field
    age1 = age.get()  # Get the value from the age entry field
    phone1 = phone_number.get()  # Get the value from the phone number entry field
    email1 = email.get()  # Get the value from the email entry field
    now = datetime.now().strftime('%y-%m-%d %H:%M:%S')  # Get the current date and time
    with open('data', 'a') as file:  # Open file in append mode
        file.write(f'||Name: {name1} || Age: {age1} || Phone: {phone1} || Email: {email1} || Time: {now} ||\n')  # Write data to the file
    name_entry.delete(0, END)  # Clear the name entry field
    age_entry.delete(0, END)  # Clear the age entry field
    phone_entry.delete(0, END)  # Clear the phone number entry field
    email_entry.delete(0, END)  # Clear the email entry field
    messagebox.showinfo("Data Entered", "Data has been entered successfully.")  # Display a message box with information

def main_screen():
    """Function to create the main application window."""
    global main, name, age, phone_number, email  # Declare global variables

    main = Tk()  # Create a new Tkinter window
    main.geometry('400x500')  # Set the size of the window
    main.title('Data Entry')  # Set the title of the window

    name = StringVar()  # Variable to store name
    age = StringVar()  # Variable to store age
    phone_number = StringVar()  # Variable to store phone number
    email = StringVar()  # Variable to store email

    Label(main, text='Enter Details', fg='red', font='calibri 15 bold').pack()  # Create a label to display title

    Label(main, text='Name:').pack()  # Create a label for name
    name_entry = Entry(main, textvariable=name, width=30)  # Create an entry field for name
    name_entry.pack()  # Place the entry field in the window

    Label(main, text='Age:').pack()  # Create a label for age
    age_entry = Entry(main, textvariable=age, width=30)  # Create an entry field for age
    age_entry.pack()  # Place the entry field in the window

    Label(main, text='Phone Number:').pack()  # Create a label for phone number
    phone_entry = Entry(main, textvariable=phone_number, width=30)  # Create an entry field for phone number
    phone_entry.pack()  # Place the entry field in the window

    Label(main, text='Email:').pack()  # Create a label for email
    email_entry = Entry(main, textvariable=email, width=30)  # Create an entry field for email
    email_entry.pack()  # Place the entry field in the window

    Button(main, text='Enter Data', command=enter_data, bg='skyblue').pack()  # Create a button to enter data
    Button(main, text='See Data', command=see_data, bg='yellow').pack()  # Create a button to see stored data
    Button(main, text='Clear Data', command=clear_data, bg='yellow').pack()  # Create a button to clear stored data
    Button(main, text='Exit', command=exit_application, bg='red').pack()  # Create a button to exit the application

    main.mainloop()  # Run the main event loop

main_screen()  # Call the main_screen function to start the application
