

class SingletonMeta(type):
    """
    A metaclass to use other classes as singleton.
    :see: https://www.datacamp.com/community/tutorials/python-metaclasses
    """

    _instances = {}
    """ A {dict} containing classes which must be a singleton. """

    def __call__(cls, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
