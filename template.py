import os
from pathlib import Path
import logging

# Logging string
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')

project_Name = 'CNN_Disease_Classifier'

File_list = [".github/workflows/.gitkeep",
             f"source/{project_Name}/__init__.py",
             f"source/{project_Name}/components/__init__.py",
             f"source/{project_Name}/utils/__init__.py",
             f"source/{project_Name}/config/__init__.py",
             f"source/{project_Name}/config/configuration.py",
             f"source/{project_Name}/pipeline/__init__.py",
             f"source/{project_Name}/entity/__init__.py",
             f"source/{project_Name}/constants/__init__.py",
             "config/config.yaml", "DVC.yaml", "Params.yaml", "requirements.txt", "setup.py", "research/trials.ipynb", "templates/index.html"]

for filepath in File_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")