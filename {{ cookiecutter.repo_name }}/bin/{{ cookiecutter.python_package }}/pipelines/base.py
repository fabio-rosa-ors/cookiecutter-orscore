from ast import Dict, List
from typing import Optional, Any
from algolite import Pipeline, Strategy, Command

class BasePipeline(Pipeline):
    def __init__(self) -> None:
        super().__init__()

    def Prepare(self, data_tag: str, shuffle: bool, check_valid_y: bool = True, override: bool = True, savefile: bool = True, session: Command = None) -> Optional[Any]:
        pass

    def SelectFeatures(self, strategy: Strategy, select_features: bool = True, features_json: bool = False, session: Command = None) -> Dict[str, List[str]]:
        pass