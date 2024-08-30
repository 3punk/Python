from tkinter import *
root = Tk()
root.geometry("300x250")

def getvals():
    print("Accepted")

# Heading
Label(root, text="Python Registration Form", font="Times 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
email = Label(root, text="Email")
birthdate = Label(root, text="Birth Date")

# Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
birthdate.grid(row=5,column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emailvalue = StringVar
birthdatevalue = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable= namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emailentry = Entry(root, textvariable = emailvalue)
birthdateentry = Entry(root, textvariable = birthdatevalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
birthdateentry.grid(row=5, column=3)

# Checkbox
checkbtn = Checkbutton(text="Remember Me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

# Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
