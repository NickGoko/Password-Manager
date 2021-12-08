from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

 
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for nums in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_output = website_input.get()
    email_output = email_input.get()
    password_output = password_entry.get()
    new_data = {website_output: {
        "email": email_output,
        "password": password_output
    }
    }
    if len(password_output) == 0 or len(website_output) == 0:
        messagebox.showwarning(title="Oops Password is insufficient", message="Please input a longer a password")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_entry.delete(0, END)


# -----------------------Find Password ------------------------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=90)

canvas = Canvas(width=200, height=188)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:", font=(FONT_NAME, 11, "bold"))
website_label.grid(column=0, row=2)

website_input = Entry(width=35)
website_input.grid(column=1, row=2, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:", font=(FONT_NAME, 11, "bold"))
email_label.grid(column=0, row=3)

email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)
email_input.delete(0, END)
email_input.insert(0, "sleipnir829@gmail.com")

password_label = Label(text="Password:", font=(FONT_NAME, 11, "bold"))
password_label.grid(column=0, row=4)

password_entry = Entry(width=21)
password_entry.grid(column=0, row=4, columnspan=3)

generate_password_button = Button(text="Generate Password", font=(FONT_NAME, 8, "bold"), command=generate_password)
generate_password_button.grid(column=2, row=4)

search_password_button = Button(text="Search", font=(FONT_NAME, 8, "bold"), command=find_password)
search_password_button.grid(column=2, row=2)

add_password_button = Button(text="Add", font=(FONT_NAME, 8, "bold"), width=36, command=save)
add_password_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
