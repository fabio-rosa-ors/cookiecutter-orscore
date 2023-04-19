from algolite import Algo

from {{ cookiecutter.python_package }}.models.base import BaseModelParams

base_strategy: Algo = Algo(
    name="base_strategy",
    algo_config=BaseModelParams(model_name="base_model"),
    split_groups_train={}
)