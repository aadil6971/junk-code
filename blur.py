# Importing The Packages
from PIL import Image
import numpy as np 
# Defining the url
url = "c:/users/aadil/pictures/123.jpeg"
# Opening the Image in memory
im = Image.open(url)
# Splitting the image into red, green, blue channels
channels = Image.Image.split(im)


kernel = np.array([[1/9 , 1/9 , 1/9],[1/9 , 1/9 , 1/9],[1/9 , 1/9 , 1/9]])

img = np.array(channels[0])

images = []
for channel in channels:
	img = np.array(channel)
	height = img.shape[0]
	width = img.shape[1]

	new_image = []
	for y in range(0,height):
		if y == 0 or y == height-1:
			pass
		else:
			new_row = []
			for x in range(0,width):
				if x == 0 or x == width-1:
					pass
				else:
					neighbours = [ [img[y-1][x-1] , img[y-1][x] ,img[y-1][x+1] ],
								   [img[y][x-1], img[y,x], img[y][x+1] ],
								   [img[y+1][x-1], img[y+1][x], img[y+1][x+1]]
								 ]
					pixel = np.sum(np.array(neighbours) * kernel)
					new_row.append(pixel)
			new_image.append(new_row)
	images.append(new_image)


finalimage = Image.merge('RGB', (Image.fromarray(np.uint8(images[0])),Image.fromarray(np.uint8(images[1])),Image.fromarray(np.uint8(images[2]))))

finalimage.show()















