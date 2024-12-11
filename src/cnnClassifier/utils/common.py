import os
import json
import yaml
import joblib
import base64
import logging
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any, Union

# Set up logging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

# Utility Functions

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other exception during file read.

    Returns:
        ConfigBox: Parsed YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        logger.error("YAML file is empty")
        raise ValueError("YAML file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(paths: Union[list, Path], verbose: bool = True):
    """Creates directories from a list or single path.

    Args:
        paths (Union[list, Path]): List of directory paths or a single path.
        verbose (bool, optional): Log directory creation. Defaults to True.
    """
    if isinstance(paths, Path):
        paths = [paths]
    
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves dictionary data to a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Dictionary data to save.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except IOError as e:
        logger.error(f"Failed to save JSON file at {path}. Error: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from the JSON file as a ConfigBox object.
    """
    try:
        with open(path) as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving binary file: {e}")
        raise e

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded successfully from: {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading binary file: {e}")
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in kilobytes.
    """
    try:
        size_in_kb = round(path.stat().st_size / 1024)
        logger.info(f"Size of {path}: {size_in_kb} KB")
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting file size: {e}")
        raise e

@ensure_annotations
def decodeImage(imgstring: str, fileName: Path):
    """Decodes a base64 image string and saves it to a file.

    Args:
        imgstring (str): Base64 encoded image string.
        fileName (Path): Path to save the decoded image.
    """
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
        logger.info(f"Image decoded and saved at: {fileName}")
    except Exception as e:
        logger.error(f"Error decoding image: {e}")
        raise e

@ensure_annotations
def encodeImageIntoBase64(imagePath: Path) -> str:
    """Encodes an image file into a base64 string.

    Args:
        imagePath (Path): Path to the image file.

    Returns:
        str: Base64 encoded image string.
    """
    try:
        with open(imagePath, "rb") as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
        logger.info(f"Image encoded from: {imagePath}")
        return encoded
    except Exception as e:
        logger.error(f"Error encoding image: {e}")
        raise e
