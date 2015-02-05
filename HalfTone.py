#!/bin/python

import cv2
import numpy as np
import sys

def halfTone(path,r=5):
	d = 2*r
	img = cv2.imread(path,0)
	height,width = img.shape
	x = [i*d+r for i in range(width/d)]
	y = [j*d+r for j in range(height/d)]
	hTone = np.zeros((height,width),np.uint8)
	for i in y:
		for j in x:
			rad = (img.item(i,j)*r)/255
			cv2.circle(hTone, (j,i), rad, 255,-1,8)
	return hTone
def display(img,maxWidth=1280,maxHeight=720):
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
	cv2.namedWindow('HalfTone')
	cv2.imshow('HalfTone',cv2.resize(img,(winWidth,winHeight)))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	try: path = sys.argv[1]
	except: path = './DataSet/image1.jpg'
	img = halfTone(path)
	display(img)




 