from dataclasses import dataclass
from pathlib import Path

# @dataclass(frozen=True)
# class DataIngestionConfig:
#     root_dir: Path
#     source_URL: str
#     locate_data_file: Path
#     unzip_dir: Path

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str