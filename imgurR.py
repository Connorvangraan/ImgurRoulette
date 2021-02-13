import urllib.request 
from PIL import Image, ImageTk
import random
from urllib.request import urlopen
from io import BytesIO
import cv2
import tkinter as tk
from tkinter import Canvas, NW
#import tkinter as tk
#from tkinter import *

def makeID():
	imgur = "https://i.imgur.com/"
	l = random.randint(0,10)
	if (l > 3):
		length = 7
	else:
		length = 5

	letters = [str(x) for x in range(0,26)]
	for i in range(0,length):
		n = random.choice(letters)

		option = random.randint(0,3)
		if(option==0):
			c = 97 + int(n)
			c = chr(c)
		elif(option==1):
			c = 65 + int(n)
			c = chr(c)
		else:
			c = random.randint(0,9)
			c = str(c)
		imgur = imgur + c
	imgur = imgur + ".jpg"
	print(imgur) 
	return imgur
	
def checkURL(url):
	urllib.request.urlretrieve(url,"img.png")
	return open("removed.png","rb").read() != open("img.png","rb").read()

def getImage(url):
	urllib.request.urlretrieve(url,"img.jpg")
	img = Image.open("img.jpg")
	img.show()
	return img


def roulette():
	imageFound = False
	count=0

	images = []

	while not imageFound:
		url = makeID()
		#url = "https://i.imgur.com/isHXMGG.jpg"

		if(checkURL(url)):
			images.append(getImage(url))
			count+=1

		if(count>0):
			imageFound=True

	return images

#images = roulette()


def testimage():
	url = "https://i.imgur.com/isHXMGG.jpg"
	urllib.request.urlretrieve(url,"img.jpg")
	img = Image.open("img.jpg")
	images=[img]
	return images




def nextFunction():
	images = roulette()
	window = tk.Toplevel()
	window.title("Imgur Roulette")
	#tk.mainloop()

	button = tk.Button(window, 
	                   text="Next", 
	                   fg="red",
	                   command=nextFunction)
	button.pack()

	canvas = Canvas(window, width = images[0].width, height = images[0].height)  
	canvas.pack()  

	img = ImageTk.PhotoImage(images[0])  
	canvas.create_image(20, 20, anchor=NW, image=img) 
	window.mainloop()


def makeWindow():
	images = testimage()
	window = tk.Tk()
	window.title("Imgur Roulette")
	#tk.mainloop()

	button = tk.Button(window, 
	                   text="Next", 
	                   fg="red",
	                   command=nextFunction)
	button.pack()

	canvas = Canvas(window, width = images[0].width, height = images[0].height)  
	canvas.pack()  

	img = ImageTk.PhotoImage(images[0])  
	canvas.create_image(20, 20, anchor=NW, image=img) 
	window.mainloop()

#makeWindow()
nextFunction()