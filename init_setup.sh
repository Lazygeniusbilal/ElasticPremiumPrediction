echo [$(date)]: "Starting the Procedure"

echo [$(date)]: "Creating a Virtual Environment"
conda create -n myvenv python=3.9 -y

echo [$(date)]: "Activating the Virtual Environment"
source activate myvenv

echo [$(date)]: "Installing all the requirements"
pip install -r requirements_dev.txt

echo [$(date)]: "Procedure Ended"