import argparse
import os 
import json

class HParams():
   def __init__(self, **kwargs):
      for k,v in kwargs.items():
        if type(v) == dict:
            v = HParams(**v)
        self[k] = v
    
    def 

def get_hparams(init = True):
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
      data = f.read()
    with open(config_save_path, "w") as f:
      f.write(data)
    
    config = json.loads(data)
    # hparams = 





