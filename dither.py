#!/bin/python

import cv2
import numpy as np
import sys
import math

def dither(img):
	"An implementation of Floyd Steinberg dithering, error diffusion dithering"
	height,width = img.shape
	out = np.zeros(img.shape,np.uint8)
	im = img.copy()
	for i in range(height-1):
		for j in range(width-1):
			old = img.item(i,j)
			new = 255 if old>127 else 0
			out.itemset(i,j,new)
			error = old-new		
			img.itemset(i,j+1,img.item(i,j+1)+error * 7/float(16))      		
      		img.itemset(i+1,j+1,img.item(i+1,j+1)+error * 3/float(16))      		
      		img.itemset(i+1,j,img.item(i+1,j)+error * 5/float(16))      		
      		img.itemset(i+1,j-1,img.item(i+1,j-1)+error * 1/float(16))
	return out


def display(img,maxWidth=1280,maxHeight=720):
	"Display function"
	height,width = img.shape
	winHeight = height
	winWidth = width
	ratio = float(winHeight)/winWidth
	if winHeight>maxHeight:
		winHeight = maxHeight
		winWidth = int(winHeight/ratio)
	if winWidth>maxWidth:
		winWidth = maxWidth
		winHeight = int(winWidth*ratio)
	cv2.namedWindow('Floyd Steinberg dithering')
	cv2.imshow('Floyd Steinberg dithering',cv2.resize(img,(winWidth,winHeight)))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	try: path = sys.argv[1]
	except: path = './DataSet/image3.jpg'
	img = cv2.imread(path,0)
	dith = dither(img)
	display(dith)