#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naver_crawling import getImage
import glob
import os

def main():

    pic_num = 50

    list_file_list = glob.glob('./data/*.txt')

    for list_file in list_file_list:
        list_file_name = list_file[7:-4]  # remove ./data, .txt string
        BASE_DIR = './NAVER/' + list_file_name
        os.mkdir(BASE_DIR)

        print (list_file+'crawling_start!!\n')
        with open(list_file,"r",encoding='UTF8') as opfd:
            for i, cd_name in enumerate(opfd):
                cd_name = cd_name[:-1]
                print(cd_name + 'start\n')
                getImage(list_file_name,cd_name,cd_name,pic_num)
                print(cd_name+'finish\n')

        print (list_file+'crawling_finish!!\n')

if __name__ == "__main__":
    main()