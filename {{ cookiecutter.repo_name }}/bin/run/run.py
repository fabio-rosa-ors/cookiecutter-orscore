
# %% [markdown]
# Import libraries and define settings

# %%
import datetime as dt
import pandas as pd
from typing import Optional, Set, Dict, List
import os
import argparse
import warnings
warnings.filterwarnings('ignore')

from {{ cookiecutter.python_package }}.helper import {{ cookiecutter.ApplicationHelper }}


my_parser = argparse.ArgumentParser()
my_parser.add_argument('--prepare-data', 	action='store', type=str, default="n")	# build-ts
my_parser.add_argument('--register-sources', 	action='store', type=str, default="n")	# 
my_parser.add_argument('--build-models', 		action='store', type=str, default="n")	# 
my_parser.add_argument('--update-models', 		action='store', type=str, default="n")	# 
my_parser.add_argument('--launch-forecast', 	action='store', type=str, default="y")	# 
my_parser.add_argument('--save-forecast', 	 	action='store', type=str, default="n")	# 
args = my_parser.parse_args()

hlp = {{ cookiecutter.ApplicationHelper }}()

if args.prepare_data == "y":
    # e.g.
    # hlp.
    pass
elif args.register_sources == "y":
    # e.g.
    # hlp.
    pass
elif args.build_models == "y":
    # e.g.
    # hlp.
    pass
elif args.update_models == "y":
    # e.g.
    # hlp.
    pass
elif args.launch_forecast == "y":
    # e.g.
    # hlp.
    pass
elif args.save_forecast == "y":
    # e.g.
    # hlp.
    pass