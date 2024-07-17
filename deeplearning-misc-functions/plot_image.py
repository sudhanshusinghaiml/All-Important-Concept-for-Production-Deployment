'''
    This is a function to plot images from a folder, subfolder and a file.
'''

import os
import random
import matplotlib.pyplot as plt
import cv2

def plot_image(folder, class_folder):
  target_path = os.path.join(folder, class_folder)
  image_dir = os.listdir(target_path)
  image_files = random.sample(image_dir, 12)

  figure, axes = plt.subplots(4,3, figsize=(20,20))

  for idx, image_filename in enumerate(image_files):
    row = idx // 3
    col = idx % 3
    image_path = os.path.join(target_path, image_filename)
    image = plt.imread(image_path)
    axes[row, col].imshow(image)
    axes[row, col].axis('off')
    idx

  plt.show()
  
 
def plot_images(images, labels):
  
  # Number of Classes
  num_classes=10
  
  # Obtaing the unique classes from y_train
  categories=np.unique(labels)
  keys=dict(labels_df['Common Name'])
  
  rows = 3   # Defining number of rows=3
  cols = 4   # Defining number of columns=4
  
  # Defining the figure size to 10x8
  fig = plt.figure(figsize=(10, 8))
  
  for i in range(cols):
      for j in range(rows):
      
          # Generating random indices from the data and plotting the images
          random_index = np.random.randint(0, len(labels))

          # Adding subplots with 3 rows and 4 columns
          ax = fig.add_subplot(rows, cols, i * rows + j + 1)

          # Plotting the image
          ax.imshow(images[random_index, :])
          
          ax.set_title(keys[random_index])
  
  plt.show()
  

'''
    This is a function to plot image from a folder, subfolder and a file 
    and to plot bounding box from annotations
'''
# Importing openCV for image processing
import cv2

# Display images using OpenCV
# Importing cv2_imshow from google.patches to display images
from google.colab.patches import cv2_imshow

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

def plot_images(image_path, image_annotations):

    # image_path = "image_data"
    # image_annotations = "annotations"
    
    for i, e in enumerate(os.listdir(image_annotations)):
        if i < 10:
            filename = e.split(".")[0]+".jpg"
            print(filename)
            img = cv2.imread(os.path.join(image_path,filename))
            df = pd.read_csv(os.path.join(image_annotations,e))
            plt.imshow(img)
            for row in df.iterrows():
                x1 = int(row[1][0].split(" ")[0])    # iterate over each row and get
                y1 = int(row[1][0].split(" ")[1])
                x2 = int(row[1][0].split(" ")[2])
                y2 = int(row[1][0].split(" ")[3])
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0), 2)
            plt.figure()
            plt.imshow(img)
            break