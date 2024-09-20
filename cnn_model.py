#import libraries

import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.layers import BatchNormalization
from keras.utils import to_categorical

#Load the data
(x_train,y_train),(x_test,y_test) = mnist.load_data()

#preprocess of data
x_train = x_train.reshape(x_train.shape[0],28,28,1).astype('float32')/255
x_test = x_test.reshape(x_test.shape[0],28,28,1).astype('float32')/255

#one-hot encoding
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

# Define the CNN model
model = Sequential()

# First convolutional layer with 32 filters, 3x3 kernel, and ReLU activation
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(BatchNormalization())

# Second convolutional layer with 64 filters, followed by MaxPooling and Dropout
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Flatten the 3D output to 1D for fully connected layers
model.add(Flatten())

# Fully connected layer with 128 units and ReLU activation
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Output layer with 10 units (one for each digit), using softmax activation
model.add(Dense(10, activation='softmax'))


# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])


# Train the model
batch_size = 128
epochs = 12

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))


# Evaluate the model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save('cnn_model.h5')
