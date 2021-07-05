from __future__ import print_function, division
import os
import torch
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import os

class MountainDataset(Dataset):
    
    '''Mountain Peaks Dataset'''
    def __init__(self, rootDir, bigRam = False, maxlen = 0):
        '''
        Args:
            root: root directory
            Naming should be same for DEM and Peak files
        '''
        self.maxlen = maxlen
        self.rootDir = rootDir
        
        self.bigRam = bigRam
        # TODO maybe load the Peak files into bool arrays. Shouldn't be to big
        if self.bigRam == True:
            #If the Mashine has big Ram images can be loaded into Ram
            #TODO load imgs
            pass
    
    def __str__(self):
        ret = "Mountain Data Set\n"
        ret += "Root directory: {self.rootDir}"
        ret += f"Length {len(self)}"
        return ret
        
    def __len__(self):
        if self.maxlen>0:
            return min((self.maxlen, len([file for file in os.listdir(self.rootDir) if file.endswith("_dem.tif")])))
        else:
            return len([file for file in os.listdir(self.rootDir) if file.endswith("_dem.tif")])
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.toList()
        if idx>len(self):
            raise ValueError
        dem_name = os.path.join(self.rootDir, f"{idx}_dem.tif")
        peaks_name = os.path.join(self.rootDir, f"{idx}_peaks.tif")
        image_dem = np.expand_dims(io.imread(dem_name), 0)
        image_peaks = np.expand_dims(io.imread(peaks_name), 0)
        
        sample = (image_dem, image_peaks)
        
        return sample
    
