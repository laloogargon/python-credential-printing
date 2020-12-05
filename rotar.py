import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=500, height=500, bg="gray")
frame1.pack()

frame2 = tk.Frame(master=window, width=250, height=50, bg="yellow")
frame2.pack()

image = Image.open("maincharacter.png")
        photo = ImageTk.PhotoImage(image.resize((196, 196), Image.ANTIALIAS))

        label = Label(top_left, image=photo, bg='green')
        label.image = photo
        label.pack()

b1 = tk.Button(frame2, text = "Rotar Izquierda", background = "red", fg = "white") 
b1.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

b2 = tk.Button(frame2, text = "Rotar Derecha", background = "blue", fg = "white") 
b2.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

window.mainloop()