import numpy as np
import cv2
import math

def calculateTiltAngle(img):
	# Code from https://stackoverflow.com/questions/46731947/detect-angle-and-rotate-an-image-in-python/46732132
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
	lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

	angles = []

	for [[x1, y1, x2, y2]] in lines:
	    # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
	    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
	    angles.append(angle)

	median_angle = np.median(angles)

	return median_angle

def deskewImage(img):
	height, width, channels = img.shape

	angle = calculateTiltAngle(img)

	M = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)
	rotated_image = cv2.warpAffine(img, M, (width, height), borderValue=(255, 255, 255))

	return rotated_image

def cropImage(img):
	# Code from https://stackoverflow.com/questions/44383209/how-to-detect-edge-and-crop-an-image-in-python
	# rsz_img = cv2.resize(img, None, fx=0.25, fy=0.25) # resize since image is huge
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
	# threshold to get just the signature
	retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
	# find where the signature is and make a cropped region
	points = np.argwhere(thresh_gray==0) # find where the black pixels are
	points = np.fliplr(points) # store them in x,y coordinates instead of row,col indices
	x, y, w, h = cv2.boundingRect(points) # create a rectangle around those points
	x, y, w, h = x-32, y-10, w+60, h+30 # make the box a little bigger
	crop = img[y:y+h, x:x+w] # create a cropped region of the gray image
	
	return crop

if __name__ == '__main__':
	img_in = cv2.imread('burro-back.png')
	img_out = deskewImage(img_in)
	crop_img = cropImage(img_out)
	# cv2.imshow('Original', img_in)
	# cv2.imshow('Salida',img_out)
	cv2.imshow('Crop', crop_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()