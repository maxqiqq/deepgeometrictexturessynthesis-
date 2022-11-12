import os

EPSILON = 1e-6
DEBUG = False
PROJECT_ROOT1 = "D:/Program Files"               #把project_root改为project_root1
#os.path.dirname(os.path.realpath(__file__))
DATA_ROOT = f'{PROJECT_ROOT1}/dgts_dataset'
#f'{PROJECT_ROOT}/dataset'
RAW_MESHES = f'{DATA_ROOT}/raw'
CACHE_ROOT = f'{DATA_ROOT}/cache'
CHECKPOINTS_ROOT = f'{PROJECT_ROOT1}/checkpoints'
