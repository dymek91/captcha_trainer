from PIL import Image
from config import *
import os
import PIL
import numpy as np
import time


def desaturate(image: Image, debug=False):
    image = image.convert('RGB')
    np_rgb = np.array(image)
    # Luminosity
    np_grey = np.multiply(np_rgb, [0.2126, 0.7152, 0.0722])
    np_grey_sum = np_grey.sum(axis=2).astype(int)
    image = Image.fromarray(np_grey_sum)
    image = image.convert('L')
    # lightness
    # return int((max(red, green, blue) + min(red, green, blue)) / 2)
    # Luminosity
    # return int(red * 0.3 + green * 0.59 + blue * 0.11)
    #ver2
    # (Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)
    return image

test_path = "D:/Programy/github-repos/kerlomz/captcha_trainer/data/test_data"
train_path = "D:/Programy/github-repos/kerlomz/captcha_trainer/data/train_data"

test_resized_path = test_path + "_resized"
train_resized_path = train_path + "_resized"

if not os.path.exists(test_resized_path):
    os.mkdir(test_resized_path)
if not os.path.exists(train_resized_path):
    os.mkdir(train_resized_path)

desired_width = RESIZE[0]
desired_height = RESIZE[1]

# test
test_dataset = [trains for trains in os.listdir(test_path)]
for image_filename in test_dataset:
    image_path = test_path + "/" + image_filename
    image = Image.open(image_path)
    ext = ".png"
    # image = image.resize((desired_width, desired_height), Image.BILINEAR)
    image = image.resize((desired_width, desired_height), Image.ANTIALIAS )
    image = desaturate(image)
    image.save(test_resized_path + "/" + image_filename.split('.')[0] + ext)

# train
train_dataset = [trains for trains in os.listdir(train_path)]
for image_filename in train_dataset:
    image_path = train_path + "/" + image_filename
    image = Image.open(image_path)
    ext = ".png"
    image = image.resize((desired_width, desired_height), Image.ANTIALIAS)
    image = desaturate(image)
    image.save(train_resized_path + "/" + image_filename.split('.')[0] + ext)
