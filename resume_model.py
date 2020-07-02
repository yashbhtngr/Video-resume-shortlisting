# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K

class CNNModel:
	@staticmethod
	def build():
		# initialize the model
		model = Sequential()
		# inputShape = (height, width, depth)

		# if we are using "channels first", update the input shape
		# if K.image_data_format() == "channels_first":
		# 	inputShape = (depth, height, width)

		# first set of CONV => RELU => POOL layers
		model.add(Conv2D(32, kernel_size=3, padding="same", activation='relu', use_bias=True, input_shape=(320,320,3)))
		model.add(Conv2D(32, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Conv2D(32, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Conv2D(64, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Conv2D(64, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Conv2D(128, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Conv2D(128, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Conv2D(256, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Conv2D(256, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Conv2D(256, kernel_size=3, padding="same", activation='relu', use_bias=True))
		model.add(Flatten())
		model.add(Dense(120, activation='relu'))
		model.add(Dense(60, activation='softmax'))

		# model.compile(loss=keras.losses.categorical_crossentropy,
		# 	optimizer=keras.optimizers.Adam(),
		# 	metrics=['accuracy'])
		# return the constructed network architecture
		print(model.summary())
		return model
