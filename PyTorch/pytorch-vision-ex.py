#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:59:52 2026

@author: yavuzkanat

DEEP LEARNING 

DATASET : MNSIT 


""" 

# %%  Load Libraries 

import torch # tensor library
 
import torch.nn as nn # artifical nerual network class 

import torch.optim as opt # optimization algortihms

import torchvision # vision processing and predefiend models

import torchvision.transforms as transforms # vision transform

import matplotlib.pyplot as plt 

# optional :  detect the GPU.

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load dataset 

def get_data_loader(batch_size = 64 ): # batch size for every iteration
      
    transform = transforms.Compose([
        transforms.ToTensor(), # Convert a PIL Image or ndarray to tensor and scale the values accordingly.
        transforms.Normalize((0.5,), (0.5,)) # Normalize a tensor image with mean and standard deviation.
        
        ])
    # download mnist dataset and train it 
    
    train_set =  torchvision.datasets.MNIST("./datasets",train=True,download=True,transform=transform)
    test_set =  torchvision.datasets.MNIST("./datasets",train=False,download=True,transform=transform)
    
    train_loader = torch.utils.data.DataLoader(train_set,batch_size=batch_size,shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_set,batch_size=batch_size,shuffle=False)
    
    return train_loader,test_loader
    
train_loader , test_loader = get_data_loader()


# %% Data Visualization


def visualize_samples(loader,n) : 
    
    images, labels = next(iter(loader)) # get images and labeles from first batch 
    
    fig , axes = plt.subplots(1,n,figsize = (10,5))
    
    
    for i in range(n):
        
        axes[i].imshow(images[i].squeeze(),cmap="gray")
        axes[i].set_title(f"Label : {labels[i].item()}")
        axes[i].axis("off")
    
    plt.show()

visualize_samples(train_loader,4)    
    
    
    
    
    
    

