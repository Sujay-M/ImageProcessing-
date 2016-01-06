#!/bin/python
import cv2
import numpy as np
import sys

def multiply(image,factor):
	_,_,channel = image.shape
	for i in range(channel):
		ch = image[:,:,i]
		ch = cv2.multiply(ch,factor)
		image[:,:,i] = ch
	return image	
def update(dummy=None):
	mul = cv2.getTrackbarPos('mul', WIN_NAME)/float(100)
	result = multiply(img.copy(),mul)
	height,width,_ = img.shape
	winHeight = height
	winWidth = width
	ratio = float(winHeight)/winWidth
	if winHeight>MAX_HEIGHT:
		winHeight = MAX_HEIGHT
		winWidth = int(winHeight/ratio)
	if winWidth>MAX_WIDTH:
		winWidth = MAX_WIDTH
		winHeight = int(winWidth*ratio)
	cv2.imshow(WIN_NAME,cv2.resize(result,(winWidth,winHeight)))
if __name__=='__main__':
	try: path = sys.argv[1]		
	except: path = './DataSet/poster1.jpg'
	img = cv2.imread(path)
	if img is None:
		print 'Failed to load image file:', path
		sys.exit(1)
	WIN_NAME='Display'
	MAX_HEIGHT=720
	MAX_WIDTH=1280
	cv2.namedWindow(WIN_NAME)
	cv2.createTrackbar('mul', WIN_NAME, 100, 1000, update)
	update()
	cv2.waitKey(0)
	cv2.destroyAllWindows()
