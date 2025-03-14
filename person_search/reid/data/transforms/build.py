# encoding: utf-8

import torchvision.transforms as T

from .transforms import RandomErasing

# 这里改成只构建验证集了
def build_transforms(cfg):
    normalize_transform = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    transform = T.Compose([
        T.Resize(cfg.INPUT.SIZE_TEST),  # resize

        T.ToTensor(),  # tensor
        normalize_transform
    ])

    return transform
