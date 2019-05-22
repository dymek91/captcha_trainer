# about captcha image
# 48 128 5
# 64 128 4
IMAGE_HEIGHT = 64
IMAGE_WIDTH = 128
CHAR_SETS = 'abcdefghijklmnpqrstuvwxyz123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 4
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'