from dataclasses import dataclasses
from pathlib import Path

@dataclasses(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    locate_data_file: Path
    unzip_dir: Path