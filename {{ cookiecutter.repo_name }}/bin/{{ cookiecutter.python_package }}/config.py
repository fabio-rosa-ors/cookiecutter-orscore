
import os
from dotenv import load_dotenv

from algolite import DSProject, PrjParams, Command, FSPath

load_dotenv()

DATA_FOLDER: str = os.getenv("DATA_FOLDER")
OUTPUT_FOLDER: str = os.getenv("OUTPUT_FOLDER")

class {{ cookiecutter.ApplicationContext}}(FSPath):
	def __init__(self, prefix_path: str = "") -> None:
		super().__init__(prefix_path)

class {{ cookiecutter.ApplicationContext }}(DSProject):
	def __init__(
		self,
		prj_conf: PrjParams 
	) -> None:
		
		super().__init__(prj_conf)

