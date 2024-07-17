'''
    This is a function to extract files and images from a zip files.
'''

import zipfile
import os

def extract_files(filepath, filename):
	
	# Specify the path to your zip file
	zip_file_path = os.path.join(filepath, filename)
    # '/content/drive/My Drive/DLDatasets/TransferLearning/monkey-dataset.zip'
	
	# Specify the directory where you want to extract the contents
	output_dir_path = '/content/drive/My Drive/DLDatasets/TransferLearning/'
	
	# Create the target directory if it doesn't exist
	os.makedirs(output_dir_path, exist_ok=True)
	
	# Extract the contents of the zip file
	with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
		zip_ref.extractall(output_dir_path)
	
	# Check the extracted files in the target directory
	output_files = os.listdir(output_dir_path)
	print("Extracted Files:", output_files)