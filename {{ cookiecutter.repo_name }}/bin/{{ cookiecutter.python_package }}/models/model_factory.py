from algolite import ModelFactory, Strategy, DataFilter

class {{ cookiecutter.ApplicationModelFactory }}(ModelFactory):
    def create_object(strategy:Strategy=None, datasplit:DataFilter=None):
        pass