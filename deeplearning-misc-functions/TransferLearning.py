'''
	Splitting the dataset
'''

from sklearn.model_selection import train_test_split

X_temp, X_test, y_temp, y_test = train_test_split(np.array(images), labels , test_size=0.1, random_state=42, stratify=labels)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp , test_size=0.1, random_state=42,stratify=y_temp)

print(X_train.shape,y_train.shape)
print(X_val.shape,y_val.shape)
print(X_test.shape,y_test.shape)


'''
    Data Augmentation
'''

# Importing the ImageDataGenerator for data augmentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1/255.0,
                                  rotation_range=0.2,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  shear_range=0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True)

valid_datagen = ImageDataGenerator(rescale=1/255.0)

test_datagen = ImageDataGenerator(rescale=1/255.0)

# Convert labels from names to one hot vectors
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)


print(X_train.shape, y_train.shape)
print(X_val.shape, y_val.shape)
print(X_test.shape, y_test.shape)


train_data = train_datagen.flow(X_train, y_train,
                               batch_size=16,
                               shuffle=True)

valid_data = valid_datagen.flow(X_val, y_val,
                                batch_size=16,
                                shuffle=True)

test_data = test_datagen.flow(X_test, y_test,
                               batch_size=16,
                               shuffle=True)
                               
                               
# Normalizing the image pixels
X_train_normalized = X_train.astype('float32')/255.0
X_val_normalized = X_val.astype('float32')/255.0
X_test_normalized = X_test.astype('float32')/255.0


from tensorflow.keras.models import Model
from tensorflow.keras.applications.densenet import DenseNet169

denseNet_model = DenseNet169(weights='imagenet', include_top = False, input_shape = (128, 128, 3))
denseNet_model.summary()


# Making all the layers of the denseNet model non-trainable. i.e. freezing them
for layer in denseNet_model.layers:
    layer.trainable = False

'''
    Convolution Neural Network - Transfer Learning Architecture
'''
tl_denseNet_model = Sequential()

# Adding the convolutional part of the VGG16 model from above
tl_denseNet_model.add(denseNet_model)

# Flattening the output of the VGG16 model because it is from a convolutional layer
tl_denseNet_model.add(Flatten())

# Adding a dense output layer
tl_denseNet_model.add(Dense(128, activation='relu'))
tl_denseNet_model.add(Dropout(0.2))
tl_denseNet_model.add(Dense(64, activation='relu'))
tl_denseNet_model.add(Dropout(0.2))
tl_denseNet_model.add(Dense(32, activation='relu'))
tl_denseNet_model.add(Dense(10, activation='softmax'))
opt=Adam()
# Compile model
tl_denseNet_model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

# Generating the summary of the model
tl_denseNet_model.summary()


# Epochs
epochs = 25
# Batch size
batch_size = 64

history_denseNet = tl_denseNet_model.fit(train_data,
                                      epochs=epochs,
                                      validation_data=(valid_data),
                                      verbose=1)
                                      

# Plotting Model Accuracy for Train and Validation Data

plt.plot(history_denseNet.history['accuracy'])
plt.plot(history_denseNet.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()


# Evaluating the model on test data
train_accuracy = tl_denseNet_model.evaluate(X_train_normalized, y_train, verbose=2)
valid_accuracy = tl_denseNet_model.evaluate(X_val_normalized, y_val, verbose=2)
test_accuracy = tl_denseNet_model.evaluate(X_test_normalized, y_test, verbose=2)


# Here we would get the output as probablities for each category
y_train_pred = tl_denseNet_model.predict(X_train_normalized)
y_val_pred = tl_denseNet_model.predict(X_val_normalized)
y_test_pred = tl_denseNet_model.predict(X_test_normalized)


from sklearn.metrics import classification_report, confusion_matrix

# Classification Report for Training Set
y_train_pred_arg=np.argmax(y_train_pred,axis=1)
y_train_arg=np.argmax(y_train,axis=1)
print(classification_report(y_train_arg, y_train_pred_arg))

# Classification Report for Validation Set
y_val_pred_arg=np.argmax(y_val_pred,axis=1)
y_val_arg=np.argmax(y_val,axis=1)
print(classification_report(y_val_arg,y_val_pred_arg))

# Classification Report for Test Set
y_test_pred_arg=np.argmax(y_test_pred, axis=1)
y_test_arg=np.argmax(y_test, axis=1)
print(classification_report(y_test_arg, y_test_pred_arg))

# Plotting the Confusion Matrix using confusion matrix() function which is also predefined tensorflow module
confusion_matrix = tf.math.confusion_matrix(y_test_arg, y_test_pred_arg)
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap( confusion_matrix, annot=True, linewidths=.4, fmt="d", square=True, ax=ax)
plt.show()


# Visualizing the predicted and correct label of images from test data
plt.figure(figsize=(2,2))
plt.imshow(X_test[2])
plt.show()
print('Predicted Label', tl_denseNet_model.predict((X_test_normalized[2].reshape(1,128,128,3))))   # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[2])                                               # using inverse_transform() to get the output label from the output vector

plt.figure(figsize=(2,2))
plt.imshow(X_test[33])
plt.show()
print('Predicted Label', tl_denseNet_model.predict((X_test_normalized[33].reshape(1,128,128,3))))  # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[33])                                              # using inverse_transform() to get the output label from the output vector

plt.figure(figsize=(2,2))
plt.imshow(X_test[36])
plt.show()
print('Predicted Label', (tl_denseNet_model.predict((X_test_normalized[36].reshape(1,128,128,3)))))  # reshaping the input image as we are only trying to predict using a single image
print('True Label', (y_test)[36])                                              # using inverse_transform() to get the output label from the output vector