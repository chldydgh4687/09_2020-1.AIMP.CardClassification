#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import expand_dims
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import glob
from tqdm import tqdm


def auto_augmentation(data):
    samples = expand_dims(data, 0)

    # width_shift_range
    datagen = ImageDataGenerator(width_shift_range=[-150,150])
    output_pic = 0
    for batch in datagen.flow(samples, save_to_dir='./augmentation_results', save_prefix='aug', save_format='jpg'):
        output_pic += 1
        if output_pic > 5:
            break
    #height_shift_range
    output_pic = 0
    datagen = ImageDataGenerator(height_shift_range=0.5)
    for batch in datagen.flow(samples, save_to_dir='./augmentation_results', save_prefix='aug', save_format='jpg'):
        output_pic += 1
        if output_pic > 5:
            break
    #horizontal and vertical flip augmentation
    output_pic = 0
    datagen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
    for batch in datagen.flow(samples, save_to_dir='./augmentation_results', save_prefix='aug', save_format='jpg'):
        output_pic += 1
        if output_pic > 4:
            break
    #random rotation augmentation
    output_pic = 0
    datagen = ImageDataGenerator(rotation_range=90)
    for batch in datagen.flow(samples, save_to_dir='./augmentation_results', save_prefix='aug', save_format='jpg'):
        output_pic += 1
        if output_pic > 5:
            break
    #random brightness augmentation
    # i = 0
    # datagen = ImageDataGenerator(brightness_range=[0.2,1.0])
    # for batch in datagen.flow(samples, save_to_dir='./augmentation_results', save_prefix='aug', save_format='jpg'):
    #     output_pic += 1
    #     if output_pic > 5:
    #         break

def main():
    # one picutre samples
    #img = load_img('./aug_sample.jpg')
    #img = img_to_array(img)

    # folder picture
    BASE_DIR = './augmentation_target/'
    for index, pic_file_name in tqdm(enumerate(glob.glob(BASE_DIR+'*.*'))):
        # folder picutre augmentation
        pic_file = load_img(pic_file_name)
        pic_file = img_to_array(pic_file)
        auto_augmentation(pic_file)

if __name__ == '__main__':
    main()
