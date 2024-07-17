# Intializing a sequential model
model = Sequential()

# Adding first conv layer with 64 filters and kernel size 3x3 , padding 'same' provides the output size same as the input size
# Input_shape denotes input image dimension of images
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(64, 64, 3)))

# Adding max pooling to reduce the size of output of first conv layer
model.add(MaxPooling2D((2, 2), padding = 'same'))

model.add(Conv2D(32, (3, 3), activation='relu', padding="same"))
model.add(MaxPooling2D((2, 2), padding = 'same'))

# flattening the output of the conv layer after max pooling to make it ready for creating dense connections
model.add(Flatten())

# Adding a fully connected dense layer with 100 neurons
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.3))
# Adding the output layer with 10 neurons and activation functions as softmax since this is a multi-class classification problem
model.add(Dense(10, activation='softmax'))

# Using SGD Optimizer
# opt = SGD(learning_rate=0.01, momentum=0.9)
opt=Adam()
# Compile model
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

# Generating the summary of the model
model.summary()



# Convert labels from names to one hot vectors
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

# Normalizing the image pixels
X_train_normalized = X_train.astype('float32')/255.0
X_val_normalized = X_val.astype('float32')/255.0
X_test_normalized = X_test.astype('float32')/255.0


# Plotting Model Accuracy for Train and Validation Data
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()


## -----------------------------------------------------------------------------------------------------------

# Evaluating the model on test data
accuracy = model.evaluate(X_test_normalized, y_test, verbose=2)

# Generating the predictions using test data
y_pred = model.predict(X_test_normalized)

## ----------------------------------------------------------------------------------------------------------

from sklearn.metrics import classification_report, confusion_matrix

# Obtaining the categorical values from y_test_encoded and y_pred
y_train_pred_arg = np.argmax(y_train_pred, axis=1)
y_train_arg = np.argmax(y_train,axis=1)

# Plotting the Confusion Matrix using confusion matrix() function which is also predefined tensorflow module
print(classification_report(y_train_arg, y_train_pred_arg))

## -----------------------------------------------------------------------------------------------------------

# Obtaining the categorical values from y_test_encoded and y_pred
y_train_pred_arg = np.argmax(y_train_pred, axis=1)
y_train_arg = np.argmax(y_train,axis=1)

# Plotting the Confusion Matrix using confusion matrix() function which is also predefined tensorflow module
confusion_matrix = tf.math.confusion_matrix(y_test_arg,y_train_pred_arg)
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap( confusion_matrix, annot=True, linewidths=.4, fmt="d", square=True, ax=ax)
plt.show()
## ------------------------------------------------------------------------------------------------------------

# Visualizing the predicted and correct label of images from test data
plt.figure(figsize=(2,2))
plt.imshow(X_test[2])
plt.show()
print('Predicted Label', tl_model_03.predict((X_test_normalized[2].reshape(1,128,128,3))))   # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[2])                                               # using inverse_transform() to get the output label from the output vector

plt.figure(figsize=(2,2))
plt.imshow(X_test[33])
plt.show()
print('Predicted Label', tl_model_03.predict((X_test_normalized[33].reshape(1,128,128,3))))  # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[33])                                              # using inverse_transform() to get the output label from the output vector

plt.figure(figsize=(2,2))
plt.imshow(X_test[36])
plt.show()
print('Predicted Label', (tl_model_03.predict((X_test_normalized[36].reshape(1,128,128,3)))))  # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[36])    