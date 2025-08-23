from dataclasses import dataclass
from pathlib import Path

# dataclass contaning url to Google drive as we are downloading data from there,
# and contains project location where the dataset needs to be stored.
@dataclass
class DataIngestionConfig:
    root_dir: Path          # artifacts  
    source_URL: str         # google drive share link to the dataset
    local_data_file: Path   # artifacts/data_ingestion/ dataset.zip
    unzip_dir: Path         # artifacts/data_ingestion


@dataclass
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_weights: str
    params_classes: int
    params_include_top: bool    