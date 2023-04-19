from dotenv import load_dotenv
import os

from algolite import PrjParams, DSProject, Algo, FSPath, BaseHelper

from {{ cookiecutter.python_package }}.config import {{ cookiecutter.ApplicationContext }}, {{ cookiecutter.ApplicationFSPath }}
from {{ cookiecutter.python_package }}.strategies.default import base_strategy
from {{ cookiecutter.python_package }}.pipelines.base import BasePipeline
from {{ cookiecutter.python_package }}.models.model_factory import {{ cookiecutter.ApplicationModelFactory }}

load_dotenv()

class {{ cookiecutter.ApplicationHelper }}(BaseHelper):
	def __init__(self) -> None:

		super().__init__()
		
		# create instance of FSPath with .env DATA_FOLDER
		# this is used by the pipelines to get the right data paths
		fs_path: FSPath = {{cookiecutter.ApplicationFSPath}}(os.getenv("DATA_FOLDER") or "")

		# init strategies
		base_stg: Algo = base_strategy 

		# assign fs_path to strategies (to get the right data paths when are used)
		base_stg.Paths = fs_path

		# define project parameters (e.g., name and strategies)
		poc_prj_config: PrjParams = PrjParams(
			name="POC",
			strategies={"base": base_stg}
		)

		poc = {{ cookiecutter.ApplicationContext }}(prj_conf=poc_prj_config)
		
		# register project in the helper
		self.add_project(poc)

		# init pipelines
		poc_pipeline = BasePipeline(fs_path=fs_path, 
									model_factory={{cookiecutter.ApplicationModelFactory}}())

		self.add_pipeline(name="poc_pipeline", obj=poc_pipeline)

		self.set_active_project("POC")

	def prepare_data(self):
		# e.g.
		# poc: DSProject = self.get_active_project()
		# poc_strategy: Algo = poc.SelectedStrategies[0]    # base_strategy
		# ppl: BasePipeline = poc.Pipelines['poc_pipeline']     # pipeline instance
		# ppl.AdjustData(strategy=poc_strategy)
		pass