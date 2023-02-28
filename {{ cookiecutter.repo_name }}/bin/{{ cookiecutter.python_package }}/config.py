
from typing import Optional

import os
from dotenv import load_dotenv

from kedro.config import ConfigLoader
from kedro.io import DataCatalog

from algolite import DSProject, PrjParams

load_dotenv()
# lettura da env:

""" 
COMMON_DATA_FOLDER serve a Luca Aimar per il cluster
"""

COMMON_DATA_FOLDER: str = os.getenv("COMMON_DATA_FOLDER")
BASE_FOLDER: str = os.getenv("BASE_FOLDER")
CONFIG_SOURCE:str = os.getenv("CONFIG_SOURCE") 

# class Config():
# 	def __init__(self):
	
# 		#
# 		# configurazione per preparare le TS delle "sku" importate da self._conf["sale"]
# 		# ../tarnsactions/sale_txn.h5" --> DATA_DIR/
# 		#
# 		self._conf["orders"] = {
# 			"data_path": BASE_FOLDER + "",
# 			"db": "",
# 			"db_table": "",
# 			"hierarchy_map": {},
# 			"resolution": "Undef",
# 			"ors_index": ["Date"],
# 			"dtypes_mapping": {
# 				"Date": "datetime",
# 				'CompanyCode': "string",
# 				'ArticleCode': "string",
# 				'Quantity': "float32",
# 				'TotalValue': "float32",
# 			},
# 			"names_mapping": {
# 				'Date': "DeliveryDate",
# 				'CompanyCode':'CompanyCode',
# 				'ArticleCode': "ArticleCode",
# 				'Quantity':'Quantity',
# 				'TotalValue':'TotalValue',
# 			},
# 			"indicators": {},
# 			"aggregation": {},
# 			"aggregation_dtypes": {},
# 			"file_prefix": "",
# 		}

# 		self._conf["orders_ts"] = {
# 			"data_path": "",
# 			"db": "",
# 			"db_table": "",
# 			"hierarchy_map": {"CompanyCode":"company", "ArticleCode":"sku"},
# 			"resolution": "W-SUN",
# 			"ors_index": ["ors_index"],
# 			"dtypes_mapping": {},
# 			"names_mapping": {
# 				'DeliveryDate': "DeliveryDate",
# 				'ArticleCode': "ArticleCode",
# 				'Quantity':'Quantity',
# 				'TotalValue':'TotalValue',
# 			},
# 			"indicators": {},
# 			"aggregation": {
# 				'Quantity':['sum'],
# 				'TotalValue':['sum'],
# 			},
# 			"aggregation_dtypes": {
# 				'Quantity': ["<f4"],
# 				'TotalValue': ["<f4"],
# 			},
# 			"file_prefix": "",
# 		}
  


class {{ cookiecutter.ApplicationContext }}(DSProject):
	def __init__(
		self,
		prj_conf: PrjParams 
	) -> None:
		
		super().__init__(prj_conf)
		# super().__init__(config_file_name, config_obj)

		# # todo: available strategies: caricare da forecast project !!!
		

		# # Initialise a ConfigLoader
		# conf_loader = ConfigLoader(conf_source=CONFIG_SOURCE)  #CATALOG_PATH)
		# # Load the data catalog configuration from catalog.yml
		# conf_catalog = conf_loader.get("catalog.yml")
		# # Create the DataCatalog instance from the configuration
		# self.catalog = DataCatalog.from_config(conf_catalog)
		# # 		
		# self.entities["companies"] = BObj(id="companies_mapping", items={}, df=None)
		# self.entities["products"]=BObj(id="products_local", items={}, df=None)
		# self.entities["orders"]=BObj(id="orders", items={}, df=None)
		# # pre load anagrafiche
		# self.Load(table_id="companies")
		# self.Load(table_id="products")


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
		dir_env = os.getenv("OUTPUT_DIR")
		if dir_env:
			dir_path = os.path.realpath(dir_env)
			res: str = os.path.join(dir_path, "_forecast_results.h5")
		return res

	# Implement only for special cases:
	#
	# def Load(self,
	# 		table_id="",
	# 		date_from=None,
	# 		date_to=None,
	# 		file_name="",
	# 		file_key="" )->Optional[pd.DataFrame]:

	# 	df:Optional[pd.DataFrame]=None
		
	# 	if (table_id in self.entities):
				
	# 		if table_id=="orders":
	# 			pass
	# 		elif table_id=="companies":
	# 			pass
	# 		elif table_id=="products":
	# 			pass
	# 		else:
	# 			df = self.catalog.load(table_id)

	# 		self.entities[table_id].df = df
	# 	return df

