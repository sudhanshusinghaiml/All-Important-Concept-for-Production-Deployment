'''
	Importing the ImageDataGenerator for Data Augmentation
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

## 
train_data = train_datagen.flow(X_train, y_train,
                               batch_size=16,
                               shuffle=True)

valid_data = valid_datagen.flow(X_val, y_val,
                                batch_size=16,
                                shuffle=True)

test_data = test_datagen.flow(X_test, y_test,
                               batch_size=16,
                               shuffle=True)