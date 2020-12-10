import cv2
import numpy as np
from tkinter import *

# src = cv2.imread('ima.png', cv2.IMREAD_UNCHANGED)

# scale_percent = 50
# width = int(src.shape[1] * scale_percent / 100)
# height = int(src.shape[0] * scale_percent / 100)
# desired_size = (width, height)

# image_front_resize = cv2.resize(src, desired_size)

# cv2.imshow('Salida', image_front_resize)
# cv2.imwrite('fot.png', image_front_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()

image = cv2.imread('ima.png')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),1.2,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))
contador = 0
while True:
	# Rotación
	contador = contador + 0.5
	if contador == 365:
		contador = 0
	M = cv2.getRotationMatrix2D((ancho//2,alto//2),contador,1)
	imageOut = cv2.warpAffine(image,M,(ancho,alto))
	cv2.imshow('frame',imageOut)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break