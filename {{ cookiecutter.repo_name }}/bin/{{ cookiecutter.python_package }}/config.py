
import os
from dotenv import load_dotenv

from algolite import DSProject, PrjParams, FSPath, Command

load_dotenv()

DATA_FOLDER: str = os.getenv("DATA_FOLDER")
OUTPUT_FOLDER: str = os.getenv("OUTPUT_FOLDER")

class {{ cookiecutter.ApplicationFSPath}}(FSPath):
	def __init__(self, prefix_path: str = "") -> None:
		super().__init__(prefix_path)

	def get_prefix_path(self, target: FSPath.FS, session: Command) -> str:
		# override original FSPaths data prefixes
		return super().get_prefix_path(target, session)
		
	def file_name(self, tag: str, target: FSPath.FS, session: Command = None) -> str:
		# override original FSPaths file_name behaviour
		return super().file_name(tag, target, session)

class {{ cookiecutter.ApplicationContext }}(DSProject):
	def __init__(
		self,
		prj_conf: PrjParams 
	) -> None:
		super().__init__(prj_conf)
