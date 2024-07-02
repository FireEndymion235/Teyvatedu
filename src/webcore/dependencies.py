

from .syscache import SystemCache
 

class GlobalState: 
    """
    GlobalState is a singleton class that holds the runtime state of the application.

    state.runtime.get('key') is equivalent to state.runtime['key']
    """
    def __init__(self):
        self.runtime = SystemCache()

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)


G_state = GlobalState()


def get_global_state() -> GlobalState:
    return G_state

