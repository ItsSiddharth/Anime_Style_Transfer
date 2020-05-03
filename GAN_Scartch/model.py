import tensorflow as tf

from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt


def generator():
	model = Sequential()
	model.add(Dense(7*7*256, use_bias=False, input_shape=(100,)))
	model.add(BatchNormalization())
	model.add(LeakyReLU())

	model.add(Reshape((7, 7, 256)))
	assert model.output_shape == (None, 7, 7, 256)

	model.add(Conv2DTranspose(128, (5,5), strides=(1,1), padding='same', use_bias=False))
	assert model.output_shape == (None, 7, 7, 128)
	model.add(BatchNormalization())
	model.add(LeakyReLU())

	model.add(Conv2DTranspose(64, (5,5), strides=(2,2), padding='same', use_bias=False))
	assert model.output_shape == (None, 14, 14, 64)
	model.add(BatchNormalization())
	model.add(LeakyReLU())

	model.add(Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
	assert model.output_shape == (None, 28, 28, 1)


	return model


generator = generator()

noise = tf.random.normal([1, 100])
generated_image = generator(noise, training=False)

plt.imshow(generated_image[0, :, :, 0], cmap='gray')