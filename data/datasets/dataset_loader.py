# encoding: utf-8
"""
@author:  liaoxingyu
@contact: sherlockliao01@gmail.com
"""

import os.path as osp
import os
import cv2
import numpy as np
from PIL import Image
from tensorboardX import SummaryWriter
from torch.utils.data import Dataset


def read_image(img_path):
    """Keep reading image until succeed.
    This can avoid IOError incurred by heavy IO process."""
    got_img = False
    if not osp.exists(img_path):
        raise IOError("{} does not exist".format(img_path))
    while not got_img:
        try:
            img = Image.open(img_path).convert('RGB')
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
        self.count = 0
    def __len__(self):
        return len(self.dataset)  # 获得数据集长度

    def __getitem__(self, index):
        img_path, pid, camid = self.dataset[index]
        img = read_image(img_path)

        if self.transform is not None:
            img = self.transform(img)
        # if self.count < 1 and 'bounding_box_train' in img_path:
        #     # 保存图像
        #     img_trans = img.permute((1, 2, 0))
        #     img_trans = img_trans.numpy()
        #     # 逆归一化
        #     mean = np.array([0.485, 0.456, 0.406])
        #     std = np.array([0.229, 0.224, 0.225])
        #     img_trans = std * img_trans + mean
        #     img_trans = np.clip(img_trans * 255.0, 0, 255).astype(np.uint8)
        #     img_trans = cv2.cvtColor(img_trans.astype(np.float32), cv2.COLOR_RGB2BGR)
        #     cv2.imwrite(f'logs/{pid}.jpg', img_trans)
        #     self.count += 1
        return img, pid, camid, img_path


