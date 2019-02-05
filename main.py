import os, sys
import cv2
import numpy as np
import scipy.misc

STRING_CHARACTERS = [" ", "░", "▓", "█"]


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114]).astype(int)

def convert2layers(img):
	hist,bins = np.histogram(img.ravel(),256,[0,256])
	rgb_value = 0
	count_value = 0
	for type in range(4):
		count_value = 0
		while count_value < (img.shape[0]*img.shape[1])/4 and rgb_value < 254:

			if hist[rgb_value] > 0:
				count_value += hist[rgb_value]
				index = np.where(img==rgb_value)
				img[index] = type

			rgb_value += 1
	print(img)
	return img

def printASCII(img):
	for columns in range(img.shape[0]):
		string = ""
		for lines in range(img.shape[1]):
			string += STRING_CHARACTERS[img[columns, lines]]
		print(string)

if __name__ == '__main__':

	image_shape = (13, 13)
	image_file = "./image.png"

	image = scipy.misc.imresize(scipy.misc.imread(image_file), image_shape)
	image = rgb2gray(image)
	print("Shape : ", image.shape)

	image = convert2layers(image)
	printASCII(image)
	scipy.misc.imsave('saved.png', image)

