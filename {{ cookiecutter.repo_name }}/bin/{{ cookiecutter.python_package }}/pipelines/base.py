from ast import Dict, List
from typing import Optional, Any
from algolite import Pipeline, Strategy, Command, FSPath

class BasePipeline(Pipeline):
    def __init__(self, fs_path: FSPath) -> None:
        super().__init__(fs_path)

    def Import(self, query_tag: str, query_filter: Any = None, override: bool = True, session: Command = None) -> None:
        return super().Import(query_tag, query_filter, override, session)

    def Prepare(self, data_tag: str, shuffle: bool, check_valid_y: bool = True, override: bool = True, savefile: bool = True, session: Command = None) -> Optional[Any]:
        pass

    def SelectFeatures(self, strategy: Strategy, select_features: bool = True, features_json: bool = False, session: Command = None) -> Dict[str, List[str]]:
        pass