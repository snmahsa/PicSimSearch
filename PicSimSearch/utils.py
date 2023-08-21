from .dependencies import *
from .variables import FEAT_FOLDER_PATH
def creat_features_dataset_path(dataset_path):
    folder_name_dataset = os.path.basename(dataset_path)
    FEAT_PATH = FEAT_FOLDER_PATH + folder_name_dataset + ".pkl"
    return FEAT_PATH