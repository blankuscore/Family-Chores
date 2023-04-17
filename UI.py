import tkinter as tk
from PIL import Image, ImageTk

# create the main window
root = tk.Tk()

def chore_select(input):
    print(input.get())
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("Chore Selection")
    new_window.geometry("480x130+800+400")

    label=tk.Label(new_window)
    label.grid(row=0,column=0)

    chore1 = tk.Button(new_window, text="Clean the cat litter", height=2)
    chore1.grid(row=1, column=0)
    chore2 = tk.Button(new_window, text="Put away clean dishes", height=2)
    chore2.grid(row=1, column=1)
    chore3 = tk.Button(new_window, text="Put away dirty dishes", height=2)
    chore3.grid(row=1, column=2)
    chore4 = tk.Button(new_window, text="Take out the trash", height=2)
    chore4.grid(row=1, column=3)

    label=tk.Label(new_window)
    label.grid(row=2,column=0)

    chore5 = tk.Button(new_window, text="Put away laundry",  height=2)
    chore5.grid(row=3, column=0)
    chore6 = tk.Button(new_window, text="Mow the lawn",  height=2)
    chore6.grid(row=3, column=1)
    chore7 = tk.Button(new_window, text="Vacuum the carpet",  height=2)
    chore7.grid(row=3, column=2)
    chore8 = tk.Button(new_window, text="Tidy your room",  height=2)
    chore8.grid(row=3, column=3)

# create an image object
image = Image.open("Images\Me\me.jpg")
image = image.resize((300, 300), Image.LANCZOS)
greg_photo = ImageTk.PhotoImage(image)

image = Image.open("Images\Alicia\IMG_5956.JPG")
image = image.resize((300, 300), Image.LANCZOS)
alicia_photo = ImageTk.PhotoImage(image)

image = Image.open("Images\Aria\IMG_5992.PNG")
image = image.resize((300, 300), Image.LANCZOS)
aria_photo = ImageTk.PhotoImage(image)

image = Image.open("Images\Mae\IMG_5983.JPG")
image = image.resize((300, 300), Image.LANCZOS)
mae_photo = ImageTk.PhotoImage(image)

root.title("Who is reporting the chore?")
root.geometry("600x600+800+300")

# create a 2x2 grid of buttons
greg_selection = tk.StringVar(value = "Greg")
greg_button = tk.Button(root, image=greg_photo, command=lambda:chore_select(greg_selection))
greg_button.image = greg_photo  # keep a reference to the photo to prevent garbage collection
greg_button.grid(row=0, column=0)

alicia_selection = tk.StringVar(value = "Alicia")
alicia_button = tk.Button(root, image=alicia_photo, command=lambda:chore_select(alicia_selection))
alicia_button.image = alicia_photo
alicia_button.grid(row=0, column=1)

aria_selection = tk.StringVar(value = "Aria")
aria_button = tk.Button(root, image=aria_photo, command=lambda:chore_select(aria_selection))
aria_button.image = aria_photo
aria_button.grid(row=1, column=0)

mae_selection = tk.StringVar(value = "Mae")
mae_button = tk.Button(root, image=mae_photo, command=lambda:chore_select(mae_selection))
mae_button.image = mae_photo
mae_button.grid(row=1, column=1)

# run the main loop
root.mainloop()
