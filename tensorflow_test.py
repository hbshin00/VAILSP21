import tensorflow as tf

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,7])

result = tf.multiply(x1, x2)

print(result)

#why doesn't this work tho
#sess = tf.Session()

#print(sess.run(result))

#sess.close()

#Belgian Traffic Signs
import os
import skimage
import imageio
import numpy as np

def load_date(data_directory):
    directories = [d for f in os.listdir(data_directory)
                    if os.path.isdir(os.path.join(data_directory, d))]

    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                    for f in os.listdir(label_directory)
                    if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "/Users/halib/Desktop/2021Spring/SureStart/BelgianTraffic"
train_data_directory = os.path.join(ROOT_PATH, "/Users/halib/Desktop/2021Spring/SureStart/BelgianTraffic/Training")
test_data_directory = os.path.join(ROOT_PATH, "/Users/halib/Desktop/2021Spring/SureStart/BelgianTraffic/Testing")

images, labels = load_data(train_data_directory)

import matplotlib.pyplot as plt

plt.hist(labels, 62)

plt.show()
