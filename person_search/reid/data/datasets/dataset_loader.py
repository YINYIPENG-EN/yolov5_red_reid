# encoding: utf-8


import os.path as osp

import cv2
from PIL import Image
from torch.utils.data import Dataset
import numpy as np


def read_image(img_path):
    """Keep reading image until succeed.
    This can avoid IOError incurred by heavy IO process."""
    got_img = False
    if not osp.exists(img_path):
        raise IOError("{} does not exist".format(img_path))
    while not got_img:
        try:
            # img = Image.open(img_path).convert('RGB')
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            img = Image.fromarray(img)
            got_img = True
        except IOError:
            print("IOError incurred when reading '{}'. Will redo. Don't worry. Just chill.".format(img_path))
            pass
    return img


class ImageDataset(Dataset):
    """Image Person ReID Dataset"""

    def __init__(self, dataset, transform=None):
        self.dataset = dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        img_path, pid, camid = self.dataset[index]
        img = read_image(img_path)  # 使用Image读取图像

        if self.transform is not None:
            img = self.transform(img)

        return img, pid, camid, img_path
