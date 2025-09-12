import os 
import yaml
import json
from box.exceptions import BoxValueError
from classifier import logger
import joblib
import base64
from typing import Any
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
        read a yaml file.

        Args:
            path_to_yaml (str): path to the yaml file
        Returns:
            ConfigBox   // Using the Config Box so we can access     values like object attributes, not just dictionary keys.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):
    """
        creates directories

        Args:
            path_to_dirs (str): path for the new directories 
            verbose (bool, optional): Ignore if multiple directories are to be created. 
    """
    for dir_path in path_to_dirs:
        os.makedirs(dir_path, exist_ok=True)

        if verbose:
            logger.info(f"Created directory at: {dir_path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
        Saves json file at the given file path
        
        Args:
            path (str): desired path for storing json file
            data (dict): data to be saved in json file
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    """
        reads a json file and returns its content

        Args:
            path: path to the json file
        Returns:
            Configbox: content of the json file
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
        saves the data into a binary file at given file location

        Args:
            data (Any): content to be saved 
            path (str): location where binary file is to be saved
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations 
def load_bin(path: Path)-> Any:
    """
        returs the content of a binary file

        Args:
            path (str): file path to the binary file 
        Returns:
            data: content of the binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path)-> str:
    """
        retuns the size of the given file 
        Args:
            path (str): path to the desired file
        Returns;
            str: size of the file in  KB (KiloBytes)
    """
    size_in_kb = round(os.path.getsize(path)/1024, 2)
    return f"~{size_in_kb} KB"

def decodImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())