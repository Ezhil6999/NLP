import math,os,random,torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import librosa,scipy

MAX_WAV_VALUE = 32768.0

def dynamic_range_compression_torch(x, C=1, clip_val = 1e-5):
    '''
    Compresses large variations in values using a log transform
    Makes small values more visible and large values less dominant
    Prevents numerical issues like log(0)

    input : x is usually a positive-valued tensor
    Examples:STFT magnitude, Mel-spectrogram , Power spectrum

    eg input : [0.000001, 0.01, 1.0, 100.0]
    eg ouput : [-11.51, -4.60, 0.0, 4.60]
    '''
    return torch.log(torch.clamp(x, min=clip_val) * C)

def dynamic_range_decompression_torch(x,C=1):
    '''
    This function converts linear magnitude values into log-scaled
     values to compress dynamic range,
     making audio features more stable and perceptually meaningful.
    '''
    return torch.exp(x) / C

def spectral_normalize_torch(magnitudes):
    output = dynamic_range_compression_torch(magnitudes)
    return output


def spectral_de_normalize_torch(magnitudes):
    output = dynamic_range_decompression_torch(magnitudes)
    return output