# We first load the necessary libraries, the dataset and reshape its dimensons to the minimum allowed by the VGG16 --> (48,48,3)
import tensorflow as tf
from keras import callbacks
from keras import optimizers
from tensorflow.keras import Input, Model
from keras.layers import Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import VGG16
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import numpy as np


input_shape = (48, 48, 3)



print("Success")