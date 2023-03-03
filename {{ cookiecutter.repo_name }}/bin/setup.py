from setuptools import find_packages, setup
import os

entry_point = (
    "{{ cookiecutter.repo_name }} = {{ cookiecutter.python_package }}.__main__:main"
)

# get the dependencies and installs
with open("requirements.txt", encoding="utf-8") as f:
    # Make sure we strip all comments and options (e.g "--extra-index-url")
    # that arise from a modified pip.conf file that configure global options
    # when running kedro build-reqs
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)
    requires.append(f'algolite @ file://localhost/{os.getcwd()}/libs/algolite-'+"{{cookiecutter.algolite_version}}"+'-py3-none-any.whl')

setup(
    name='{{ cookiecutter.python_package }}',
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": [entry_point]},
    install_requires=requires,
)
