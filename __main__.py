from singleton import Singleton, ReturnOption


class Universe(metaclass=Singleton):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Universe(age={self._age})"


Universe.if_already_initialized(ReturnOption.NONE)
# Universe.if_already_initialized(ReturnOption.INSTANCE)
# Universe.if_already_initialized(ReturnOption.EXCEPTION)

universe_1 = Universe(10)
universe_2 = Universe(5)

print(universe_1)
print(universe_2)
