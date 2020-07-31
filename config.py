import ast
import os

# select the type of the model here
from models.wavenet import Model, hparams

# names:
DATA_PATH = []
for dataset in ['A','B','C','D','E','F']:
    DATA_PATH.append('./data/'+dataset+'/formatted/')

SPLIT_TABLE_PATH = './data/fold_split/'
SPLIT_TABLE_NAME = 'split_table.json'

PIC_FOLDER = './data/pictures/'
DEBUG_FOLDER = './data/CV_debug/'

for f in [PIC_FOLDER, DEBUG_FOLDER]:
    os.makedirs(f, exist_ok=True)