import tkinter as tk
from PIL import Image, ImageTk

# create the main window
root = tk.Tk()

def printcmd(input):
    print(input.get())
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("Chore Selection")
    new_window.geometry("600x100+800+400")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()


# create an image object
image = Image.open("Images\Me\me.jpg")
image = image.resize((300, 300), Image.LANCZOS)
photo1 = ImageTk.PhotoImage(image)

image = Image.open("Images\Alicia\IMG_5956.JPG")
image = image.resize((300, 300), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(image)

image = Image.open("Images\Aria\IMG_5992.PNG")
image = image.resize((300, 300), Image.LANCZOS)
photo3 = ImageTk.PhotoImage(image)

image = Image.open("Images\Mae\IMG_5983.JPG")
image = image.resize((300, 300), Image.LANCZOS)
photo4 = ImageTk.PhotoImage(image)

root.title("Who is reporting the chore?")
root.geometry("600x600+800+300")

# create a 2x2 grid of buttons
entry_string1 = tk.StringVar(value = "Greg")
button1 = tk.Button(root, image=photo1, command=lambda:printcmd(entry_string1))
button1.image = photo1  # keep a reference to the photo to prevent garbage collection
button1.grid(row=0, column=0)

entry_string2 = tk.StringVar(value = "Alicia")
button2 = tk.Button(root, image=photo2, command=lambda:printcmd(entry_string2))
button2.image = photo2
button2.grid(row=0, column=1)

entry_string3 = tk.StringVar(value = "Aria")
button3 = tk.Button(root, image=photo3, command=lambda:printcmd(entry_string3))
button3.image = photo3
button3.grid(row=1, column=0)

entry_string4 = tk.StringVar(value = "Mae")
button4 = tk.Button(root, image=photo4, command=lambda:printcmd(entry_string4))
button4.image = photo4
button4.grid(row=1, column=1)

# run the main loop
root.mainloop()
