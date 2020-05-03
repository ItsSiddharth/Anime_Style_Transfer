import os

import numpy as np
import cv2




def generate_outline(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.resize(image, (256, 256))
	edges = cv2.Canny(image, 100, 100)
	edges = cv2.bitwise_not(edges)
	# edges = np.array(edges)
	return edges


def black_and_white(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.resize(image, (256, 256))
	# image = np.array(image)
	return image

def colour_output(image):
	image = cv2.resize(image, (256, 256))
	# image = np.array(image)
	return image





list_of_names = [filename for filename in os.listdir('gallery-dl/danbooru/3611_images_withbody') if filename.endswith('.jpg')]
# or filename.endswith('.png')
print(len(list_of_names))


# list_of_names = list_of_names[:60000]
i=0
edge_data = []
bandw_data = []
colour_data = []
for file in list_of_names:
	try:
		# print(file)
		image = cv2.imread('gallery-dl/danbooru/3611_images_withbody/{}'.format(file))
		edges = generate_outline(image)
		# print(type(edges))
		# print(edges.shape)
		# blackandwhite = black_and_white(image)
		# colourimage = colour_output(image)
		# colour_data.append(colourimage)
		# bandw_data.append(blackandwhite)
		edge_data.append(edges)
		print(i)
		i=i+1
	except:
		print("Not Readable")
# final = np.array(final)
edge_data = np.array(edge_data)
print(len(edge_data))
# colour_data = np.array(colour_data)
# bandw_data = np.array(bandw_data)

np.save('edge_dataset_anime.npy', edge_data)
# np.save('colour_dataset_anime.npy', colour_data)
# np.save('bandw_dataset_anime.npy', bandw_data)


# np_load_old = np.load
# np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
# final = np.load('dataset_anime.npy')
# print(len(final))
# np.load = np_load_old


# cv2.imshow('preview', final[0])
# cv2.waitKey(0)