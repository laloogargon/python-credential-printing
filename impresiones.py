import cv2
import numpy as np
from tkinter import *

src = cv2.imread('ima.png', cv2.IMREAD_UNCHANGED)

scale_percent = 50
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
desired_size = (width, height)

image_front_resize = cv2.resize(src, desired_size)

cv2.imshow('Salida', image_front_resize)
cv2.imwrite('fot.png', image_front_resize)
cv2.waitKey()
cv2.destroyAllWindows()

# top = Tk()

# C = Canvas(top, bg="blue", height=250, width=300)
# filename = PhotoImage(file = "ima.png")
# background_label = Label(top, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# C.pack()
# top.mainloop()
