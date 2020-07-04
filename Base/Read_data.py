import yaml
import os
def read_data(file_name):
    file_path = (".") + os.sep + "Data" + os.sep + file_name + ".yml"
    with open(file_path,"r",encoding="utf-8") as f:
        return yaml.load(f)