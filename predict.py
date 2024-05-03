import argparse
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(prog='biohack')
    parser.add_argument('img_path')
    args = parser.parse_args()
    return args.img_path

def predict_tumor(model, img_path):
    classes = ['glioma', 'meningioma', 'notumor', 'pituitary']
    img = Image.open(img_path).resize((299, 299))
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(2, 1, 2)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    prob = list(pred[0])
    bars = plt.barh(classes, prob)
    plt.xlabel('Probability')
    plt.gca().bar_label(bars, fmt='%.2f')
    plt.show()

if __name__ == '__main__':
    predict_tumor(load_model('biohack-model.keras'), parse_args())