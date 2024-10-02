import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "MLProject"
list_of_files = [
    
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_training.py",
    f"src/{package_name}/components/model_evaluation.py",
    f"src/{package_name}/logger/__init__.py",
    f"src/{package_name}/logger/logger.py",
    f"src/{package_name}/exception/__init__.py",
    f"src/{package_name}/exception/exception.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/common.py",
    ".gitignore",
    "README.md",
    "setup.py",
    "init_setup.sh",
    "requirements_dev.txt",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")   