# FEAT_PATH = None
from .dependencies import os

#get directory path
project_dir = os.getcwd()
#Creat features dataset path
folder_name = "features/"
folder_path = os.path.join(project_dir, folder_name)
FEAT_FOLDER_PATH = folder_path

##########################

#creat Image folder path
DEFAULT_FOLDER_PATH  = os.path.join(project_dir, '/Images/')
