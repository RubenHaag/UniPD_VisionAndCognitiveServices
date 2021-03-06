## Unet Implementation by Ruben Haag


# Pytorch functions
import torch
# Neural network layers
import torch.nn as nn
import torch.nn.functional as F
# Optimizer
import torch.optim as optim
# Handling dataset|
import torch.utils.data as data
# Torchvision library
import torchvision

import matplotlib.pyplot as plt
import numpy as np
import copy
import time
import os
import cv2
# For results
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


#Recreate UNEt as used in the Paper
class UNet(nn.Module):
    def __init__(self, n_classes):
        
        super(UNet, self).__init__()
        
        self.l1_feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU()
        )
        
        self.l2_feature_extractor = nn.Sequential(
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1),
            nn.ReLU()
        )
        
        self.l3_feature_extractor = nn.Sequential(
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1),
            nn.ReLU()
            
        )
        self.l3_up = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        
        self.l2_mapgenerator = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1),
            nn.ReLU()
        )
        self.l2_up = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.l1_mapgenerator = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU(),
#TODO: Is that correct? Why two output channels? We only have one feature or not? Maybe Mountain and not Mountain?
            nn.Conv2d(kernel_size=1, in_channels=64, out_channels=n_classes, stride = 1),
        )
    
    def forward(self, x):
        
        l1 = self.l1_feature_extractor(x)
        
        l2 = self.l2_feature_extractor(l1)
        l3 = self.l3_feature_extractor(l2)
        
        l3 = self.l3_up(l3)
        #Cropping of second level
        
        dX = l2.size()[2] - l3.size()[2]
        dY = l2.size()[3] - l3.size()[3]
        l2 = l2[:,:, dX//2: l2.size()[2]-dX//2, dY//2: l2.size()[3]-dY//2]
        l2 = torch.cat([l2, l3], dim=1)
        del l3
        
        #Generate l2 Map
        l2 = self.l2_mapgenerator(l2)
        l2 = self.l2_up(l2)
        # Do the same for level 1
        #Cropping of third level
        dX = l1.size()[2] - l2.size()[2]
        dY = l1.size()[3] - l2.size()[3]
        l1 = l1[:,:, dX//2: l1.size()[2]-dX//2, dY//2: l1.size()[3]-dY//2]
        l1 = torch.cat([l1, l2], dim=1)
        
        del l2

        l1 = self.l1_mapgenerator(l1)
        return l1
    
    def save_model(self, path):
        torch.save(self, path)
        
