from algolite import Strategy

from {{ cookiecutter.python_package }}.models.base import BaseModelParams

base_strategy: Strategy = Strategy(
    name="base_strategy",
    algo_config=BaseModelParams(model_name="base_model"),
    split_groups_train={}
)