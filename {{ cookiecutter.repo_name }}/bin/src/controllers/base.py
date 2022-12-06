from typing import Dict, List, Set, Optional
import pandas as pd
import datetime as dt
# dipendenze da orscore: 
from orscore.data_handler.symbol_handler import SymbolID
from orscore.types_global import ResolutionEnum, check_end_date
from orscore.types_global import ResolutionEnum
# dipendenze da orscore.server:
from orsserver.ts_helper import TSController
# dipendenze da progetto "custom":
from bin.src.config import {{ cookiecutter.ApplicationContext }}

class {{ cookiecutter.ApplicationController }}(TSController):
    # """Class with common methods"""

    def  __init__(
        self,
        context: {{ cookiecutter.ApplicationContext }},
    ) -> None:
        """Initialize a controller with:
        - project (ORSCoreProject): the current ML project already opened
        - context (DMContext): the context of the current project
        - parser (Callable): callable method to parse the requested data_path key.
                            If BaseDMController is instantiated by orsserver.BaseHelper,
                             the parser should be the method 'parse_keys' implemented in the project's helper.
        """
        # il padre-basecontroller (non)ha property DMContext !
        super().__init__(context) #, parser)
        
   
