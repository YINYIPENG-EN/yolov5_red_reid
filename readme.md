**本项目为红外场景下的行人重识别**

(**说明：**本项目为有偿项目，按功能收取费用，可按自己需求购买~

关于售后：对于基础理论部分可**免费**讲解，可**免费**远程调试程序和答疑，帮你省去不必要的时间~联系方式可看文末)



**收费部分：**

1.训练核心代码(含tensorboard)

2.GUI界面

3.跨多视频检测(无GUI)

以上三个功能均独立，可按需求购买。

------

**准备代码：**

```shell
git clone https://github.com/YINYIPENG-EN/yolov5_red_reid.git
```



ps:arrow_right:**该训练reid项目与person_search项目是独立的！！**训练完reid后，把训练好的权重放到person_search/weights下，切换到peron_search项目中在去进行reid识别【不然有时候会报can't import xxx】。



**数据集准备**

通过网盘分享的文件：CASIA-Markt.zip
链接: https://pan.baidu.com/s/11h6j0Hu0D3JFHKpOG5acpg 提取码: twpv 

# 训练

## 配置文件说明

**train.py参数说明如下：**

--config_file: 配置文件路径，默认configs/softmax_triplet.yml

--weights: pretrained weight path

--neck:  If train with BNNeck, options: **bnneck** or no

--test_neck:  BNNeck to be used for test, before or after BNNneck options: **before** or **after**

--model_name: Name of backbone.

--pretrain_choice: Imagenet

--IF_WITH_CENTER: us center loss, True or False.

--resume:resume train

--freeze: freeze train

--freeze_epoch: freeze train epochs 

:fountain_pen:

配置文件的修改：

(注意：**项目中有两个配置文件，一个是config下的defaults.py配置文件，一个是configs下的yml配置文件**，**一般配置yml文件即可**，当两个配置文件参数名相同的时候以yml文件为主，这个需要注意一下)

**configs文件**:

以**softmax_triplet.yml**为例：

```
SOLVER:
  OPTIMIZER_NAME: 'Adam' # 优化器
  MAX_EPOCHS: 120  # 总epochs
  BASE_LR: 0.00035
  IMS_PER_BATCH: 8  # batch
TEST:
  IMS_PER_BATCH: 4 # test batch
  RE_RANKING: 'no'
  WEIGHT: "path"  # test weight path
  FEAT_NORM: 'yes'
OUTPUT_DIR: "/logs" # model save path
```

## 快速开启训练

```shell
python tools/train.py

```

开启训练后打印如下：

```
Loading pretrained ImageNet model......


2023-02-24 21:08:22.121 | INFO     | engine.trainer:log_training_loss:194 - Epoch[1] Iteration[19/1484] Loss: 9.194, Acc: 0.002, Base Lr: 3.82e-05
2023-02-24 21:08:22.315 | INFO     | engine.trainer:log_training_loss:194 - Epoch[1] Iteration[20/1484] Loss: 9.156, Acc: 0.002, Base Lr: 3.82e-05
2023-02-24 21:08:22.537 | INFO     | engine.trainer:log_training_loss:194 - Epoch[1] Iteration[21/1484] Loss: 9.119, Acc: 0.002, Base Lr: 3.82e-05


```



## 中断后的继续训练或微调训练

如果训练意外终止，或者希望继续训练，可以使用本功能。只需要传入--resume参数即可

```shell
python tools/train.py --weights 【your weight path】 --resume

```

```shell
环境说明：

matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
pytorch-ignite=0.4.11
```

## 冻结训练

新增冻结训练，加快网络前期训练速度。

训练中只需传入：--freeze    --freeze_epoch 20即可，其中--freeze表示是否开启冻结训练，--freeze_epoch是冻结训练后的epoch，这里默认为20，那么网络会在前20个epoch冻结训练，从21个epoch开始解冻训练

示例如下：

```bash
python tools/train.py --weights your weigt path --freeze --freeze_epoch 20
```



# 测试

输入以下命令即可快速开启测试，获得测试结果

【此脚本是针对训练后的模型单独获得测试结果，例如mAP、Rank等指标】
```

python tools/test.py --weights weights/ReID_resnet50_ibn_a.pth

```

测试结果如下：

```
Validation Results
mAP: 56.4%
CMC curve, Rank-1  :85.7%
CMC curve, Rank-5  :92.2%
```



#  训练预权重下载：

将 **r50_ibn_2.pth，resnet50-19c8e357.pth**放在yolov5_red_reid/weights下

链接：https://pan.baidu.com/s/1QYvFE6rDSmxNl4VBNBar-A 
提取码：yypn

# 联系方式：
微信直接搜：y24065939s
或CSDN文末二维码添加：https://blog.csdn.net/z240626191s/article/details/146266998?sharetype=blogdetail&sharerId=146266998&sharerefer=PC&sharesource=z240626191s&spm=1011.2480.3001.8118
