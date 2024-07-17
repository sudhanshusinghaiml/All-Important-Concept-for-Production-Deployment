loaded_images = np.load('images.npy', allow_pickle=True)
print(loaded_images.shape)

images_list = []
image_metadata_list = []

for index, values in enumerate(loaded_images):
  images_list.append(loaded_images[index][0])
  data = loaded_images[index][1]

  image_metadata = {}
  # Iterate over the list of dictionaries
  for idx, item in enumerate(data):
    for key, value in item.items():
      if key == 'label':
        image_metadata[f'label_{idx + 1}'] = item['label']
        image_metadata[f'label_{idx + 1}'] = item['label']
      elif key == 'points':
        # Flatten the 'points' list of dictionaries
        for point_num, point in enumerate(item['points']):
          image_metadata[f'point_x_{idx + 1}{point_num + 1}'] = point['x']
          image_metadata[f'point_y_{idx + 1}{point_num + 1}'] = point['y']
      elif key == 'imageWidth':
        image_metadata[f'imageWidth_{idx + 1}'] = item['imageWidth']
      elif key == 'imageHeight':
        image_metadata[f'imageHeight_{idx + 1}'] = item['imageHeight']

      else:
        image_metadata[key] = value

  # Append the dictionary to the list
  image_metadata_list.append(image_metadata)

# Convert list of dictionaries to DataFrame
metadata_df = pd.DataFrame(image_metadata_list)
images_df = pd.DataFrame({ 'images': images_list })

# Concatenating both dataframe
df = pd.concat([images_df, metadata_df], axis=1)

# Display the DataFrame
df.head()