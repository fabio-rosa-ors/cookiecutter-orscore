from algolite import ModelFactory, Algo, DataFilter

class {{ cookiecutter.ApplicationModelFactory }}(ModelFactory):
    def create_object(strategy:Algo=None, datasplit:DataFilter=None):
        pass