# Importing the required libraries

import tensorflow
from tensorflow import keras
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import concatenate

from tensorflow.keras.model import Model, Sequential



# Building the Convolution Block

def custom_convolution(pre_layer_output, no_of_filter=64):
  # Taking first input and implementing the first convolution block
  conv_output_1 = Conv2D(no_of_filter, kernel_size = (3, 3), activation= 'relu', padding='same') (pre_layer_output)
  batch_norm_output_1 = BatchNormalization() (conv_output_1)

  # Taking first input and implementing the second conv block
  conv_ouput_2 = Conv2D(no_of_filter, kernel_size = (3, 3), activation= 'relu', padding='same') (batch_norm_output_1)
  batch_norm_output_2 = BatchNormalization() (conv_ouput_2)

  return batch_norm_output_2

# Constructing the downsampling/encoder blocks
def custom_encoder(prev_layer_output, no_of_filter = 64):
  # Collect the start and end of each sub-block for normal pass and skip connections
  custom_conv_output = custom_convolution(prev_layer_output, no_of_filter)
  max_pool_output = MaxPooling2D(pool_size = (2, 2)) (custom_conv_output)
  return custom_conv_output, max_pool_output


# Constructing the upsampling/decoder blocks
def custom_decoder(prev_layer_output, skip, no_of_filter = 64):
  # Upsampling and concatenating the essential features
  upsample_output = Conv2DTranspose(no_of_filter, kernel_size = (2,2), padding='same') (prev_layer_output)
  skip_conn_output = Concatenate()([upsample_output, skip])
  decoder_output = custom_convolution(skip_conn_output, no_of_filter)
  return decoder_output
  

# Construct the U-Net architecture:

def U_Net(ImageSize):
    
    # Take the image size and shape
    input1 = Input(ImageSize)
    
    # Construct the encoder blocks
    skip_output_1, encoder_output_1 = custom_encoder(input1, 64)
    skip_output_2, encoder_output_2 = custom_encoder(encoder_output_1, 64*2)
    skip_output_3, encoder_output_3 = custom_encoder(encoder_output_2, 64*4)
    skip_output_4, encoder_output_4 = custom_encoder(encoder_output_3, 64*8)
    
    # Preparing the next block
    conv_block_output = custom_convolution(encoder_output_4, 64*16)
    
    # Construct the decoder blocks
    decoder_output_1 = custom_decoder(conv_block_output, skip_output_4, 64*8)
    decoder_output_2 = custom_decoder(decoder_output_1, skip_output_3, 64*4)
    decoder_output_3 = custom_decoder(decoder_output_2, skip_output_2, 64*2)
    decoder_output_4 = custom_decoder(decoder_output_3, skip_output_1, 64)
    
    final_output = Conv2D(1, 1, padding="same", activation="sigmoid")(decoder_output_4)

    model = Model(input1, final_output)
    return model