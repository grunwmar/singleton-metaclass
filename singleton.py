from enum import Enum, auto
""" Singleton """


class ReturnOption(Enum):

    NONE = auto()
    EXCEPTION = auto()
    INSTANCE = auto()


class SingletonException(Exception):
    ...


class Singleton(type):
    """ Singleton metaclass """

    __instance = None
    __if_initialized_option = None

    @classmethod
    def if_already_initialized(cls, option: ReturnOption):
        cls.__if_initialized_option = option

    def __call__(mcs, *args, **kwargs):
        """ Checks if instance of metaclass' derivative exists. """
        """ If so, prevents creating of another instance. """

        option = mcs.__class__.__if_initialized_option

        if mcs.__class__.__instance is None:
            mcs.__class__.__instance = super().__call__(*args, **kwargs)
            return mcs.__class__.__instance
        else:
            if option == ReturnOption.INSTANCE:
                return mcs.__class__.__instance
            elif option == ReturnOption.EXCEPTION:
                raise SingletonException(f"Instance of class '{mcs.__name__}' already exists. ")
            else:
                return None
