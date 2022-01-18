#%%
from glob import glob
# Built-in imports
import os, datetime, pathlib, random 
from glob import glob
import math
from math import ceil, floor

# Basic imports
import numpy as np
import pandas as pd   

# Ploting libraries
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (10,10)
mpl.rcParams['axes.grid'] = False
#%matplotlib inline

import seaborn as sns
sns.set(color_codes=True)

import PIL
from PIL import Image
import skimage
from skimage import color, io
#from skimage import data
from skimage import transform

# Tensorflow imports
import tensorflow as tf
print(f'Tensorflow version is: {tf.version.VERSION}')
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  print('GPU device not found')
print('Found GPU at: {}'.format(device_name))

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image as kp_image
from tensorflow.keras.callbacks import TensorBoard 
from tensorflow.keras import applications, optimizers, models, losses, layers
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
#from tensorflow.keras.metrics import 

# Train-test-split and evaluation imports
#from sklearn.model_selection import train_test_split # If required
#from sklearn import metrics # classification report
#from sklearn.metrics import confusion_matrix, classification_report
#from sklearn.model_selection import KFold


predictor = tf.keras.models.load_model(
    str(path_project_dir.joinpath('models','model_4.h5'))
    )

# arabic labels 
arabic_labels = {0: 'Alif', 1: 'Ayeen', 2: 'Baa', 3: 'Daal', 4: 'Faa', 5: 'Ghaeen', 6: 'Haa', 7: 'Jeem', 8: 'Kaaf', 9: 'Khaa', 10: 'Laam', 11: 'Meem', 12: 'Nuun', 13: 'Qouf', 14: 'Raa', 15: 'Saa', 16: 'Seen', 17: 'Sheen', 18: "Su'ad", 19: 'Taa', 20: 'Tuaa', 21: 'Waoo', 22: 'Yaa', 23: 'Zaal', 24: 'Zazza', 25: "Zu'ad", 26: 'Zua', 27: 'huu'}
# approximation - alphabet to arabic
alphabet_to_arabic = {'a': 'Alif','b': 'Baa','f': 'Faa','r': 'Ghaeen','h': 'Haa','j': 'Jeem','k': 'Kaaf','l': 'Laam','m': 'Meem','n': 'Nuun','q': 'Qouf','r': 'Raa','s': 'Saa','t': 'Taa','u': 'Waoo','i': 'Yaa','z': 'Zaal'}
# approximation - arabib to alphabet
arabic_to_alphabet = {v:k for k,v in alphabet_to_arabic.items()}

prediction = 

tf.compat.v1.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))


style_content = glob(str(path_to_images)+'/*', recursive = True)
path_styles = glob(style_content[0] + '/*')
path_content = glob(style_content[1] + '/*')

print(path_styles)
print()
print(path_content)