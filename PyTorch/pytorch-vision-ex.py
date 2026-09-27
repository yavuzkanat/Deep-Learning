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

import matplotlib as plt 

# optional :  detect the GPU.

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load dataset 

def get_data_loader(batch_size = 64 ): # batch size for every iteration
      
    transform = transforms.Compose([
        transforms.ToTensor(), # Convert a PIL Image or ndarray to tensor and scale the values accordingly.
        transforms.Normalize((0.5,), (0.5,)) # Normalize a tensor image with mean and standard deviation.
        
        ])
    

