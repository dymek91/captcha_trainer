from PIL import Image
from config import *
import os

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
    ext = ".jpeg"
    image = image.resize((desired_width, desired_height), Image.BILINEAR)
    image.save(test_resized_path + "/" + image_filename.split('.')[0] + ext)

# train
train_dataset = [trains for trains in os.listdir(train_path)]
for image_filename in train_dataset:
    image_path = train_path + "/" + image_filename
    image = Image.open(image_path)
    ext = ".jpeg"
    image = image.resize((desired_width, desired_height), Image.BILINEAR)
    image.save(train_resized_path + "/" + image_filename.split('.')[0] + ext)
