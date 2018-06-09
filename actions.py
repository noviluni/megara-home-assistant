

class ModuleException(Exception):
    pass


class ModuleMixin:

    orders = []
    # requirements = []

    @classmethod
    def set_up(cls):
        pass
