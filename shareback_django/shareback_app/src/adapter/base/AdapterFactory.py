class AdapterFactory:

    unique_instance = None

    @staticmethod
    def get_instance():

        if AdapterFactory.unique_instance is None:
            AdapterFactory.unique_instance = AdapterFactory()

        return AdapterFactory.unique_instance
