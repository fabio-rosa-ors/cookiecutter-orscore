from algolite import Algo

from {{ cookiecutter.python_package }}.models.base import BaseModelParams

base_strategy: Algo = Algo(
    name="base_strategy",
    model_config=BaseModelParams(model_name="base_model", cats=[], nums=[], do_feature_selection=False, param={}),
    split_groups={}
)