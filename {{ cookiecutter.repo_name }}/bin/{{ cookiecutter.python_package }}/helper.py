from dotenv import load_dotenv
import datetime as dt
from typing import List

from {{ cookiecutter.python_package }}.config import {{ cookiecutter.ApplicationContext }}
from {{ cookiecutter.python_package }}.controllers.base import {{ cookiecutter.ApplicationController }}

from orsserver.helper import BaseHelper

load_dotenv()

#
class {{ cookiecutter.ApplicationHelper }}(BaseHelper):
	def __init__(self) -> None:
		super().__init__(prj_conf={}, req_conf=req_conf)

		# initialize application context and project
		self._ctx = {{ cookiecutter.ApplicationContext }}.Build()

		# initialize controllers
		self._ctl["ts"] = {{ cookiecutter.ApplicationController }}(self.Context)

		# resource keys accessibili tramite get_available_resources
		# ...

		# initialize active project
		self.set_active_project("POC")

	def create_update_data(self, json) -> bool:
		"""Create/Update the data of a list of resource keys"""
		keys: List[str] = json.get("resource_keys")

		prj_name:str = json.get("project") or self._prj_name
		
		status: bool = False
		return self.cmd_create_update_data(prj_name=prj_name, keys=keys)

	def cmd_create_update_data(self, prj_name, keys:List[str]) -> bool:
		prj_name:str = prj_name or self._prj_name

		print("Start update...")
		start_run = dt.datetime.now()
		self.set_active_project(prj_name=prj_name)
		
		self._ctl["ts"].create_update_data(keys)
