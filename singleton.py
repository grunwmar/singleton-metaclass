from enum import Enum, auto
""" Singleton """






class SingletonException(Exception):
    """ Exception raised when instance of of singleton already exists """
    """ and if_already_initialized is set to ReturnOption.EXCEPTION """

    def __init__(self, mcs):
        class_name = mcs.__name__
        super().__init__(f"Instance of class '{class_name}' already exists. ")


class Singleton(type):
    """ Singleton metaclass """

    class AlreadyInitialized(Enum):
        """ Enum of options to input to if_already_initialized(option) """

        RETURN_NONE = auto()
        RETURN_INSTANCE = auto()
        RAISE_EXCEPTION = auto()

    __instance = None
    __if_initialized_option = None


    @classmethod
    def if_already_initialized(cls, option: AlreadyInitialized):
        cls.__if_initialized_option = option


    def __call__(mcs, *args, **kwargs):
        """ Checks if instance of metaclass' derivative exists. """
        """ If so, prevents creating of another instance. """

        option = mcs.__class__.__if_initialized_option

        # prevents call Singleton() if __instance is not none
        if mcs.__class__.__instance is None:
            mcs.__class__.__instance = super().__call__(*args, **kwargs)
            return mcs.__class__.__instance

        # do action selected in __if_initialized_option
        else:
            if option == mcs.AlreadyInitialized.RETURN_INSTANCE: # return already existing instance
                return mcs.__class__.__instance

            elif option == mcs.AlreadyInitialized.RAISE_EXCEPTION:
                raise SingletonException(mcs)

            else:
                return None
