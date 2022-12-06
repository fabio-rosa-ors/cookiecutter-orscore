
from typing import Optional

# import orscore.data_processor as odp
import datetime as dt
import pandas as pd
import os
from os import environ
from dotenv import load_dotenv
from PreliminaryAnalysis.context import ApplicationConfig, ApplicationContext, StrategyItem, BOEntity

# from src.entity.contact import Contact

from kedro.config import ConfigLoader
from kedro.io import DataCatalog

# from src.entity.ensemble import produce_contact_list, read_contact_list_from_file


load_dotenv()
# lettura da env:

""" 
COMMON_DATA_FOLDER serve a Luca Aimar per il cluster
"""

COMMON_DATA_FOLDER: str = environ["COMMON_DATA_FOLDER"] or ""
BASE_FOLDER: str = environ["BASE_FOLDER"] or ""

class {{ cookiecutter.ApplicationConfig }}(ApplicationConfig):
	def __init__(self, content):
		super().__init__(content)
	
		#
		# configurazione per preparare le TS delle "sku" importate da self._conf["sale"]
		# ../tarnsactions/sale_txn.h5" --> DATA_DIR/
		#
		self._conf["orders"] = {
			"data_path": BASE_FOLDER + "",
			"db": "",
			"db_table": "",
			"hierarchy_map": {},
			"resolution": "Undef",
			"ors_index": ["Date"],
			"dtypes_mapping": {
				"Date": "datetime",
				'CompanyCode': "string",
				'ArticleCode': "string",
				'Quantity': "float32",
				'TotalValue': "float32",
			},
			"names_mapping": {
				'Date': "DeliveryDate",
				'CompanyCode':'CompanyCode',
				'ArticleCode': "ArticleCode",
				'Quantity':'Quantity',
				'TotalValue':'TotalValue',
			},
			"indicators": {},
			"aggregation": {},
			"aggregation_dtypes": {},
			"file_prefix": "",
		}

		self._conf["orders_ts"] = {
			"data_path": "",
			"db": "",
			"db_table": "",
			"hierarchy_map": {"CompanyCode":"company", "ArticleCode":"sku"},
			"resolution": "W-SUN",
			"ors_index": ["ors_index"],
			"dtypes_mapping": {},
			"names_mapping": {
				'DeliveryDate': "DeliveryDate",
				'ArticleCode': "ArticleCode",
				'Quantity':'Quantity',
				'TotalValue':'TotalValue',
			},
			"indicators": {},
			"aggregation": {
				'Quantity':['sum'],
				'TotalValue':['sum'],
			},
			"aggregation_dtypes": {
				'Quantity': ["<f4"],
				'TotalValue': ["<f4"],
			},
			"file_prefix": "",
		}
  


class {{ cookiecutter.ApplicationContext }}(ApplicationContext):
	@staticmethod
	def Build() -> Optional["{{ cookiecutter.ApplicationContext }}"]:
		if ApplicationContext._reference is None:
			# create empty config obj
			dm_conf = {{ cookiecutter.ApplicationConfig }}({})
			# start from dmconfig and fill with ENV
			dm_conf = ApplicationContext._build_from_env(conf=dm_conf)
			# setup in appcontext
			ApplicationContext._reference = {{ cookiecutter.ApplicationContext }}(config_obj=dm_conf)
		return ApplicationContext.Ref()

	def __init__(
		self, config_file_name: str = "", config_obj: Optional[ApplicationConfig] = None
	) -> None:

		super().__init__(config_file_name, config_obj)

		# todo: available strategies: caricare da forecast project !!!
		if not hasattr(self, "_strategy_map"):
			self._strategy_map = {}
		self._strategy_map["orders"] = StrategyItem(name="orders", frequency="W-SUN")
		

		# Initialise a ConfigLoader
		conf_loader = ConfigLoader(conf_source=BASE_FOLDER+"/conf")
		# Load the data catalog configuration from catalog.yml
		conf_catalog = conf_loader.get("catalog.yml")
		# Create the DataCatalog instance from the configuration
		self.catalog = DataCatalog.from_config(conf_catalog)
		# 		
		self.entities["companies"] = BOEntity(id="companies_mapping", items={}, df=None)
		self.entities["products"]=BOEntity(id="products_local", items={}, df=None)
		self.entities["orders"]=BOEntity(id="orders", items={}, df=None)
		# pre load anagrafiche
		self.Load(table_id="companies")
		self.Load(table_id="products")


	def filename(self, key: str = "", sto="", dep="") -> str:
		name = ""
		pre = "" if sto == "" else sto  # self.fileprefix(key)
		if key ==  "orders":
			name = f"{pre}orders_txn.h5"
		elif key ==  "orders_ts":
			name = f"{pre}orders_ts.h5"
			
		return name

	def forecast_project_name(self) -> str:
		res = "_forecast"
		return res

	def forecast_output(self) -> str:
		res = ""
		dir_env = environ["OUTPUT_DIR"] or ""
		if dir_env:
			dir_path = os.path.realpath(dir_env)
			res: str = os.path.join(dir_path, "_forecast_results.h5")
		return res

	def Load(self,
			table_id="",
			date_from=None,
			date_to=None,
			file_name="",
			file_key="" )->Optional[pd.DataFrame]:

		df:Optional[pd.DataFrame]=None
		
		if (table_id in self.entities):
				
			if table_id=="orders":
				pass
			elif table_id=="companies":
				pass
			elif table_id=="products":
				pass
			else:
				df = self.catalog.load(table_id)

			self.entities[table_id].df = df
		return df

