import time
import os
import random
import numpy as np
import torch
import torch.nn as nn
from .utils.utils import load_filepath_and_text
from scipy.io.wavfile import read
import torch
import numpy as np

class TextAudioLoader(torch.utils.data.Dataset):
    def __init__(self,audio_path, hyper_params):
        self.audio_path_and_text = load_filepath_and_text(audio_path)
        self.text_cleaners = hyper_params.text_cleaners
        # Most audio processing pipelines work with 16-bit PCM audio:
        # 16-bit signed integer range:
        # −32768 to +32767
        # The maximum possible magnitude is 32768
        # So this value is used as a normalization factor.
        # 1️⃣ Converting int16 audio → float wav_float = wav_int16 / 32768.0
        # 2️⃣ Converting float → int16 (saving WAV) -> wav_int16 = wav_float * 32768.0
        # used for normalizing audio 
        self.max_wav_value = hyper_params.max_wav_value
        self.sampling_rate  = hyper_params.sampling_rate
        self.filter_length  = hyper_params.filter_length  
        self.hop_length  = hyper_params.hop_length     
        self.win_length = hyper_params.win_length

        self.cleaned_text = getattr(hyper_params,"cleaned_text", False)   

        self.add_blank = hyper_params.add_blank
        self.min_text_len = getattr(hyper_params,"min_text_len",1)
        self.max_text_len = getattr(hyper_params,"max_text_len",190)

        random.seed(1234)
        random.shuffle(self.audio_path_and_text)
        self._filter()

    def _filter(self):
        audiopaths_and_text_new = []
        lengths = []

        for audiopath,text in self.audio_path_and_text:
            if self.min_text_len <= len(text) and len(text) <= self.max_text_len:
                audiopaths_and_text_new.append([audiopath,text])
                lengths.append(os.path.getsize(audiopath) // (2*self.hop_length))
        self.audio_path_and_text = audiopaths_and_text_new
        self.length = lengths
    
    def get_audio_text_pair(self, audiopath_and_text):
        audiopath,text = audiopath_and_text[0],audiopath_and_text[1]
        text = self.get_text(text)
        spec,wav = self.get_audio(audiopath)
        return (text,spec,wav)
    
    def get_audio(self,audio_path):
        sr , data = read(audio_path)
        assert sr == self.sampling_rate, f"audio sample rate {sr} is not match with the training data"
        torch_data = torch.FloatTensor(data.astype(np.float32))

        audio_norm = torch_data / self.max_wav_value
        audio_norm = audio_norm.unsqueeze(0)
        spec_filename = audio_path.replace(".wav",".spec.pt")
        if os.path.exists(spec_filename):
            spec = torch.load(spec_filename)
        else:
            spec = 




if __name__ == "__main__":
    obj = TextAudioLoader("C:\Users\Ezhil\Downloads\LJSpeech-1.1\LJSpeech-1.1")
    
