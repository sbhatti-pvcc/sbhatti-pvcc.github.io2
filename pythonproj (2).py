from tkinter import *
import base64

#  window
root = Tk()
root.geometry('1280x720')
root.resizable(0, 0)
root.configure(bg="lightblue")

# Title of the window
root.title("Message Encode and Decode")

# Label
Label(root, text='MESSAGE ENCODE DECODE', font='comicsans 30 bold').pack()

#  variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#  encode
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#  decode
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


# set mode
def Mode():
    message = Text.get()
    key = private_key.get()

    #  checks
    if len(message) > 20:
        Result.set("Error: Message too long!")
        return
    if any(char in "@!#$%^&*(){}[]:;\"'<>,.?/|\\~`" for char in message):
        Result.set("Error: Special characters not allowed in message!")
        return
    if len(key) > 6:
        Result.set("Error: Key too long!")
        return

    if mode.get() == 'e':
        Result.set(Encode(key, message))
    elif mode.get() == 'd':
        Result.set(Decode(key, message))
    else:
        Result.set('Invalid Mode')


# exit window
def Exit():
    root.destroy()


#  reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Message input
Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

# Key input
Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key, bg='ghost white').place(x=290, y=90)

# Mode input
Label(root, font='arial 12 bold', text='MODE (e-encode, d-decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(x=290, y=120)

# Result output
Entry(root, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

# Result button
Button(root, font='arial 10 bold', text='OUTPUT', padx=2, bg='lightgrey', command=Mode).place(x=60, y=150)

# Reset button
Button(root, font='arial 10 bold', text='RESET', width=6, command=Reset, bg='LimeGreen', padx=2).place(x=120, y=240)

# Exit button
Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit, bg='OrangeRed', padx=2, pady=2).place(x=240, y=240)

# Run the application
root.mainloop()
