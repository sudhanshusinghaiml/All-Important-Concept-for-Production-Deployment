'''
    This is a function to load images from a folder, subfolder and images
    and loads the images in the form of  NumPy array to .npy files.
    
    The function also loads the labels for each of the images into a dataframe.
'''

import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Importing openCV for image processing
import cv2

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

images_list = []
labels_list = []
desired_width = 128
desired_height = 128

def load_monkey_dataset(root_folder, labels_info):

    # Iterate through each folder in the root folder
    for folder_name, subfolders, folders in os.walk(root_folder):
        
        # Iterate through each subfolder
        for folder in subfolders:
          # Iterating through subfolder 
          sub_sub_folder = os.path.join(folder_name, folder)
          image_names = sorted(os.listdir(sub_sub_folder))

          # Iterate through each image in the subfolder
          for image_name in image_names:
            if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_path = os.path.join(sub_sub_folder, image_name)

                    # Read the image using OpenCV (cv2)
                    image = cv2.imread(image_path)

                    # Convert BGR to RGB
                    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    # Resize or preprocess the image if needed
                    img_resized = cv2.resize(image, (desired_width, desired_height))

                    # Append image data and corresponding label
                    images_list.append(img_resized)
                    labels_list.append(folder)

    # Convert lists to numpy arrays
    image_np_array = np.array(images_list)
    labels_np_array = np.array(labels_list)

    # Merging the labels with common names
    labels_df = pd.DataFrame(labels_np_array, columns =['Label'])
    merged_df = pd.merge(labels_df, labels_info, on='Label', how='left')
    labels_df['Common Name'] = merged_df[' Common Name                   ']

    # Use LabelEncoder to convert string labels to numerical values
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels_np_array)
    labels_df['encoded_labels'] = encoded_labels

    # Save the Image NumPy array to a .npy file
    image_output_file = '/content/drive/My Drive/DLDatasets/TransferLearning/monkeyImages.npy'
    np.save(image_output_file, image_np_array)

    # Save the Labels to a CSV file
    labels_output_file = '/content/drive/My Drive/DLDatasets/TransferLearning/monkeyImageLabels.csv'
    labels_df.to_csv(labels_output_file, index=False)

    # Print a message indicating the successful creation of the .npy file
    print("Images successfully saved to", image_output_file)


    return image_np_array, labels_np_array, labels_df