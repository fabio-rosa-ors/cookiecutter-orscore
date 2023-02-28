from dotenv import load_dotenv
import datetime as dt
from typing import List

from algolite.project import PrjParams, DSProject, Strategy
from algolite.helper import BaseHelper

from {{ cookiecutter.python_package }}.config import {{ cookiecutter.ApplicationContext }}
from {{ cookiecutter.python_package }}.strategies.default import base_strategy
from {{ cookiecutter.python_package }}.pipelines.base import BasePipeline

load_dotenv()
# Datapath keys configuration
req_conf = {}
#
class {{ cookiecutter.ApplicationHelper }}(BaseHelper):
	def __init__(self) -> None:

		# initialize and register available projects
		poc = {{ cookiecutter.ApplicationContext }}(prj_config=PrjParams(
			name="POC", 
			candidate_strategies={"base_strategy": base_strategy}))
		
		# register project
		self.add_project(poc)

		# register pipelines (default: add the pipeline to all available projects)
		self.add_pipeline(name="poc_pipeline", obj=BasePipeline)

		self.set_active_project("POC")

	def prepare_data(self):
		# e.g.
		# poc: DSProject = self.get_active_project()
		# poc_strategy: Strategy = poc.SelectedStrategies[0] # base_strategy
		# ppl: BasePipeline = poc._ppl['poc_pipeline']()     # pipeline instance
		# ppl.AdjustData(strategy=poc_strategy)
		pass