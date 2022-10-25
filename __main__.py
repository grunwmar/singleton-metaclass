from singleton import Singleton


class Universe(metaclass=Singleton):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Universe(age={self._age})"


# Optional setting of return action
# Universe.if_already_initialized(IfAlreadyInitialized.RETURN_NONE)
# Universe.if_already_initialized(IfAlreadyInitialized.RETURN_INSTANCE)
Universe.if_already_initialized(Singleton.AlreadyInitialized.RETURN_INSTANCE)

universe_1 = Universe(10)
universe_2 = Universe(5)

print(universe_1)
print(universe_2)
