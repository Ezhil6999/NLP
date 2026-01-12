import argparse
import os 
import json

class HParams():
    def __init__(self, **kwargs):
      for k,v in kwargs.items():
        if type(v) == dict:
            v = HParams(**v)
        self[k] = v
    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()
    
    def __len__(self):
        return len(self.__dict__)
    
    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return self.__dict__.__repr__()
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)


def get_hparams():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        type=str,
        default="C:\Ezhil\NLP\audio\vits_eats\config\config.json",
        help = "path of your lj speech data set directory"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="vits_training_test_1"
    )
    args = parser.parse_args()
    model_dir = os.path.join(".","logs",args.model)
    os.makedirs(model_dir,exist_ok=True)

    config_path = args.config
    config_save_path = os.path.join(model_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.loads(f)
    with open(config_save_path, "w") as f:
        config = json.dump(config,f)
    
    Hprams = HParams(**config)
    Hprams.model_dir = model_dir
    return Hprams




