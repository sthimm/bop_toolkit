# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague

"""Configuration of the BOP Toolkit."""

import os
from dotenv import load_dotenv

######## Basic ########
load_dotenv() 

# Folder with the BOP datasets.
datasets_path = os.getenv("DATA_DIR", 'dataset')

# Folder with pose results to be evaluated.
results_path = os.getenv("RESULTS_DIR", 'results')

# Folder for the calculated pose errors and performance scores.
eval_path = os.getenv("EVAL_DIR", 'eval')

######## Extended ########

# Folder for outputs (e.g. visualizations).
output_path = os.getenv("OUTPUT_DIR", 'output')

# For offscreen C++ rendering: Path to the build folder of bop_renderer (github.com/thodan/bop_renderer).
bop_renderer_path = r"/path/to/bop_renderer/build"

# Executable of the MeshLab server.
meshlab_server_path = r"/path/to/meshlabserver.exe"

# Number of workers for the parallel evaluation of pose errors.
num_workers = 10

# use torch to calculate the errors
use_gpu = False
