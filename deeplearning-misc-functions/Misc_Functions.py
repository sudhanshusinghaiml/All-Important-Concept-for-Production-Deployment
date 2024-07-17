'''
    This is to decrease image size using openCV
'''

images_decreased=[]
height = 64
width = 64
dimensions = (width, height)
for i in range(len(images)):
  images_decreased.append( cv2.resize(images[i], dimensions, interpolation=cv2.INTER_LINEAR))
  
  
'''
    Normalizing the image pixels
'''
X_train_normalized = X_train.astype('float32')/255.0
X_val_normalized = X_val.astype('float32')/255.0
X_test_normalized = X_test.astype('float32')/255.0


'''
    Convert labels from names to one hot vectors
'''
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)


'''
    Splitting the dataset
'''
from sklearn.model_selection import train_test_split

X_temp, X_test, y_temp, y_test = train_test_split(np.array(images_decreased), labels , test_size=0.1, random_state=42, stratify=labels)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp , test_size=0.1, random_state=42,stratify=y_temp)


print(X_train.shape,y_train.shape)
print(X_val.shape,y_val.shape)
print(X_test.shape,y_test.shape)


'''
    Latest usage of IoU. Need to explore further
'''
model.compile(
  optimizer='sgd',
  loss='mse',
  metrics=[tf.keras.metrics.IoU(num_classes=10)])