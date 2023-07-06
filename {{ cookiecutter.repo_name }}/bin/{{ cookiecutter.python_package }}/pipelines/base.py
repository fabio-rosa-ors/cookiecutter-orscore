from ast import Dict, List
from typing import Optional, Any
from algolite import Pipeline, Algo, Command, FSPath, ModelFactory, Project

class BasePipeline(Pipeline):
    def __init__(self, fs_path: FSPath, model_factory: Optional[ModelFactory] = None) -> None:
        super().__init__(fs_path)

    def Import(self, query_tag: str, prj: Project | None = None, query_filter: Any = None, override: bool = True, session: Command | None = None) -> Dict[str, DataSrc] | None:
        return super().Import(query_tag, prj, query_filter, override, session)
    
    def Prepare(self, data_tag: str, shuffle: bool, algo: Algo, prj: Project | None = None, check_valid_y: bool = True, override: bool = True, savefile: bool = True, session: Command | None = None) -> Dict[str, DataSrc] | None:
        return super().Prepare(data_tag, shuffle, algo, prj, check_valid_y, override, savefile, session)
    
    def SelectFeatures(self, algo: Algo, session: Command | None = None) -> Dict[str, List[str]]:
        return super().SelectFeatures(algo, session)