from typing import Optional
from dataclasses import dataclass
from algolite import ModelInterface, Strategy, DataFilter, ModelParams

@dataclass
class BaseModelParams(ModelParams):
    pass

class BaseModel(ModelInterface):
    def __init__(self, strategy: Optional[Strategy] = None, data_filter: Optional[DataFilter] = None) -> None:
        super().__init__(strategy, data_filter)

    def Fit_Model(self, _data_tag: Optional[str] = None, save_model: bool = True):
        pass

    def Predict(self, _data_tag: Optional[str] = None, model: Any = None, _model_tag: Optional[str] = None, **kwargs):
        pass

    def Select_Features(self, _data_tag: Optional[str] = None):
        pass