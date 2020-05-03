import cv2
import numpy as np

def generate_outline(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.resize(image, (256, 256))
	edges = cv2.Canny(image, 100, 100)
	edges = cv2.bitwise_not(edges)
	edges = np.array(edges)
	return edges


def black_and_white(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.resize(image, (256, 256))
	image = np.array(image)
	return image

def colour_output(image):
	image = cv2.resize(image, (256, 256))
	image = np.array(image)
	return image


edges = generate_outline(cv2.imread('test.png'))
blackandwhite = black_and_white(cv2.imread('test.png'))
colour_output = colour_output(cv2.imread('test.png'))


cv2.imwrite('edges.jpg', edges)
cv2.imwrite('final.jpg', colour_output)

# danbooru_2950012_eb20c8ba8bcf778a152b67cbfc314d9d.png