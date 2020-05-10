import os
import tempfile
import urllib

import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
from keras.applications.densenet import DenseNet201
from keras.applications.inception_v3 import InceptionV3
from keras.applications.nasnet import NASNetLarge
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.applications.vgg16 import VGG16
from keras.applications.xception import Xception
from keras.preprocessing import image


def get_html_page(url):
    page = requests.get(url)
    return page


def get_lines_from_html(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    lines = str(soup).split('\r\n')
    return lines


def get_image_from_url(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    try:
        resp = urllib.request.urlopen(url)
        image_array = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # return the image
        return image
    except Exception as e:
        return None


def get_synset_urls(imagenet_url):
    html = get_html_page(imagenet_url)
    return get_lines_from_html(html)


def download_images_to_dir(dir_path, urls, limit=5):
    for url in urls:
        image = get_image_from_url(url)
        if image is None:
            continue
        if len(image.shape) == 3:
            output_path = os.path.join(dir_path, 'img_' + str(limit) + '.jpg')
            cv2.imwrite(output_path, image)
            if limit <= 0:
                break
            limit -= 1


def make_synsets_dirs(base_dir_path, synsets):
    for name in synsets:
        urls = get_synset_urls(synsets[name])
        synset_path = os.path.join(base_dir_path, name)
        os.mkdir(synset_path)
        download_images_to_dir(synset_path, urls)


def make_validation_synset(dir_path):
    synsets = {
        'ambulance':
            'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02701002',

        'basketball':
            'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02802426',

        'sputinik':
            'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04290615',

        'husky':
            'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02109961'
    }
    make_synsets_dirs(dir_path, synsets)


resnet50 = ResNet50(weights='imagenet', include_top=True)
vgg16 = VGG16(weights='imagenet', include_top=True)
inceptionv3 = InceptionV3(weights='imagenet', include_top=True)
xception = Xception(weights='imagenet', include_top=True)
nasnet = NASNetLarge(weights='imagenet', include_top=True)
densenet201 = DenseNet201(weights='imagenet', include_top=True)


def apply_resnet50(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = resnet50.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('ResNet50 predicted:', decode_predictions(preds, top=3)[0])


def apply_vgg16(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = vgg16.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('VGG16 predicted:', decode_predictions(preds, top=3)[0])


def apply_inceptionv3(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = inceptionv3.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('InceptionV3 predicted:', decode_predictions(preds, top=3)[0])


def apply_xception(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = xception.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('Xception predicted:', decode_predictions(preds, top=3)[0])


def apply_nasnet(img_path):
    img = image.load_img(img_path, target_size=(331, 331))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = nasnet.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('NASNet predicted:', decode_predictions(preds, top=3)[0])


def apply_densenet(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = densenet201.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    print('DenseNet201 predicted:', decode_predictions(preds, top=3)[0])


def apply_models(file_path):
    apply_resnet50(file_path)
    apply_vgg16(file_path)
    apply_inceptionv3(file_path)
    apply_xception(file_path)
    apply_nasnet(file_path)
    apply_densenet(file_path)


def main():
    with tempfile.TemporaryDirectory() as dir_path:
        make_validation_synset(dir_path)

        for path, subdirs, files in os.walk(dir_path):
            for file_name in files:
                file_path = os.path.join(path, file_name)
                print(file_path)
                apply_models(file_path)
            print('\n')


if __name__ == '__main__':
    main()
