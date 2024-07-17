from google.colab import drive
drive.mount('/content/drive')

import os

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# set working directory
os.chdir('/content/drive/My Drive/DLDatasets/ObjectDetection')

# Print the current working directory
print("Current Working Directory:", os.getcwd())

