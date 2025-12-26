# from pathlib import Path
import os
import zipfile
import gdown
from source.CNN_Disease_Classifier import logger
from source.CNN_Disease_Classifier.utils.common import get_size
from source.CNN_Disease_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Attempts to fetch data from a local path first,
        falling back to the URL if the local path is unavailable.
        """
        try:
            # 1. Define the destination for the file to end up (artifacts folder)
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            # 2. TRY: Check if the local_source_path exists and is a file
            # Assuming 'local_source_path' is added to your Config
            local_path = Path(self.config.local_source_path)

            if not local_path.exists():
                raise FileNotFoundError("Local file not found, switching to download...")

            logger.info(f"Local file found at {local_path}. Copying to {zip_download_dir}...")
            shutil.copy(local_path, zip_download_dir)
            logger.info(f"Successfully ingested data from local source.")

        except Exception as e:
            # 3. EXCEPT: Fallback to internet download
            logger.warning(f"Could not ingest locally due to: {e}")

            dataset_url = self.config.source_URL
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            try:
                # Extracting ID from Google Drive URL
                file_id = dataset_url.split("/")[-2]
                prefix = 'https://drive.google.com/uc?/export=download&id='
                gdown.download(prefix + file_id, zip_download_dir)
                logger.info(f"Downloaded data from internet into {zip_download_dir}")
            except Exception as download_error:
                logger.error(f"Failed to download from internet: {download_error}")
                raise download_error

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file to {unzip_path}")
