
# %% [markdown]
# Import libraries and define settings

# %%
import datetime as dt
import numpy as np
import pandas as pd
import janitor
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
from bin.src.helper import {{ cookiecutter.ApplicationHelper }}

hlp = {{ cookiecutter.ApplicationHelper }}()
hlp.cmd_create_update_data(prj_name="", keys=["orders"])

