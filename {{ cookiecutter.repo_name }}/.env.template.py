# Environment variables go here, can be read by `python-dotenv` package:
#
#   `src/script.py`
#   ----------------------------------------------------------------
#    import dotenv
#
#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
#    dotenv_path = os.path.join(project_dir, '.env')
#    dotenv.load_dotenv(dotenv_path)
#   ----------------------------------------------------------------
#
# Qui configurazione Dev una volta definita
#
#
#
# user specific:
BASE_FOLDER=        "/path/to/{{ cookiecutter.repo_name}}/data/"
COMMON_DATA_FOLDER= "/path/to/{{ cookiecutter.repo_name}}/data/"
DATA_DIR=           "/path/to/{{ cookiecutter.repo_name}}/data/"
OUTPUT_DIR=         "/path/to/{{ cookiecutter.repo_name}}/data/out"
TRACKING_DIR=       "/path/to/{{ cookiecutter.repo_name}}/data/tracking_files"
CONFIG_SOURCE =     "/path/to/{{ cookiecutter.repo_name}}/bin/run/conf"
CATALOG_PATH =      "/path/to/{{ cookiecutter.repo_name}}/bin/run/conf/base/catalog.yml"

PLUGIN_DIR = ""

# server specific options:
DATE_RANGE_MIN = "2022-01-30"

DB_HOST = "localhost"
DB_PORT = 27017
QUERY_TIMEOUT = "60000"
OBJECT_COUNTER = "0"

LOG_TOPICS = "[]"
LOG_STORE_TYPE = "MEM"
OBJECT_STORE_TYPE = "MEM_DICT"
PRJ_STORE_TYPE = "MONGODB"

HOST = "0.0.0.0"
PORT = 5001

# DO NOT ADD THIS FILE TO VERSION CONTROL!
DATA_FOLDER =     "/path/to/{{ cookiecutter.repo_name}}/data"
OUTPUT_FOLDER =   "/path/to/{{ cookiecutter.repo_name}}/data"
Forecast_folder = "/path/to/{{ cookiecutter.repo_name}}/data/out"
