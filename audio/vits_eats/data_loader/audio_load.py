import time
import os
import random
import numpy as np
import torch
import torch.nn as nn
from .utils.utils import load_filepath_and_text

class TextAudioLoader(torch.utils.data.Dataset):
    def __init__(self,audio_path, hyper_params):
        self.audio_path_and_text = load_filepath_and_text(audio_path)
        self.text_cleaners = 


if __name__ == "__main__":
    obj = TextAudioLoader("C:\Users\Ezhil\Downloads\LJSpeech-1.1\LJSpeech-1.1")
    
