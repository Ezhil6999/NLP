import torch, math
import torch.nn as nn
import torch.nn.functional as F
from dataclasses import dataclass
from typing import Optional, Literal, Union
from safetensors.torch import save_file

class LoRALayerBase:
    def __init__(self,
                 rank = 8,
                 lora_alpha = 8,
                 lora_dropout = 0.0,
                 use_rslora = True):
        self.rank = rank
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.use_rslora = use_rslora

