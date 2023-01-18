# Cookiecutter ORS Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](https://github.com/ORSGroup/cookiecutter-orscore)
#### [Original project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/ORSGroup/cookiecutter-orscore


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── out            <- The otcomes from model runs.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── (models)           <- TBD: Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks
│
├── (references)       <- Data dictionaries, manuals, and all other explanatory materials.
│
│
│
├── bin                <- Source code for use in this project.
|   ├── <pkg>
|   |    |
│   │    ├── __init__.py           <- Makes src a Python module
│   │    │
│   │    ├── controllers           <- Scripts to download or generate data
│   │    │   └── make_dataset.py
│   │    │
│   │    ├── entity                <- Scripts to turn raw data into features for modeling
│   │    │   └── build_features.py
│   │    │
│   │    └── tests                 <- Scripts to train models and then use trained models to make predictions
│   │        ├── predict_model.py
│   │        └── train_model.py
|   |
|   ├── requirements.txt           <- The requirements file for reproducing the analysis environment, e.g.
|   ├── setup.py                   <- makes project pip installable (pip install -e .) so src can be imported
│   |                              generated with `pip freeze > requirements.txt`
│   └── run
│   │
│   └── server
│   │
│   └── gui                        <- Scripts to create exploratory and results oriented visualizations
│       └── app.py
│
└── tox.ini                        <- (?) tox file with settings for running tox; see tox.readthedocs.io
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
