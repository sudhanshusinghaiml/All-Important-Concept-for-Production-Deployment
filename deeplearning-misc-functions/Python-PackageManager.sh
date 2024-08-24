# Package Management using Poetry

# To install poetry
pip install poetry

# To create a project structure using poetry
poetry new `project_name`

# To add the dependencies list
poetry add langchain

# To check the poetry env or setup poetry info
poetry env info

# To create the venv using project name
poetry shell

# To install all the dependencies and create lock file
poetry install

# To list local packages that has been used in our project 
pip list

# To add test files for dev, test based on environment etc
poetry add pytest --group dev

# We can also add the formatter such as black, flake8 etc.
poetry add black --group dev

# We can remove the dependencies using poetry
poetry remove langchain

# To exit the poetry vitual environment
exit

# To list all the environments using poetry
poetry env list

# To remove the poetry env from machine
poetry env remove `project_name`


# -----------------------------------------------------------------------------------------------#
# Run below command if you are running conda Environment setup for first time
# https://conda.io/projects/conda/en/latest/commands/init.html
conda init --all

# Commands to Setup Conda Environment using Command Prompt
conda create -p .venv/ python=3.10.14 -y

conda create -n hate-sppech-classification python=3.10.14 -y

conda create -n chest-disease-classification python=3.10.14 -y

# Commands to remove Conda Environment using Command Prompt
conda remove -n chest-disease-classification --all


# To activate conda environment
conda activate 

# Renaming the conda environment using 4 step process

conda activate Google-PaLM-and-Langchain-based-QnA-System

conda create --name QnA-System-using-geminipro-and-langchain --clone Google-PaLM-and-Langchain-based-QnA-System

conda deactivate Google-PaLM-and-Langchain-based-QnA-System

conda activate geminipro-and-langchain-based-QnA-System

conda remove --name Google-PaLM-and-Langchain-based-QnA-System --all


# create the requirement.txt files and update all the libraries that is needed for the project
# run the requirement.txt files using below commands
pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------------------------#

# Commands to Setup Environment using Git Bash
python -m venv .venv/

source .venv/Scripts/activate  #run this command to activate venv and change directory back to project folder

pip install -r requirements.txt

or 

pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------------------------#

# Commands to set environment variables such as API Key etc.
Create .env file in the root directory

# Set the variables in .env file
OPENAI_API_KEY = ''

# Use the below codes to load the passowrd in py or ipynb files
import os
from dotenv import load_dotenv, find_dotenv

# Checking if the .env is loaded or not - Returns True
_ = load_dotenv(find_dotenv())


# Seeting the Environment Variables
openai.api_key  = os.getenv('OPENAI_API_KEY')
# ------------------------------------------------------------------------------------------------#

Open the command palette in VS Code (Ctrl+Shift+P or Cmd+Shift+P on macOS), then type and select Python: `Select Interpreter`. 
See if your Conda environment appears in the list. If it does, select it.