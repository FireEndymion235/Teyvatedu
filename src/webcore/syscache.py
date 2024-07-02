
class SystemCache(dict):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SystemCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = {}
    def delete(self, key):
        del self._data[key]
    def update(self, key, value):   
        self._data[key] = value
    def create(self, key, value):
        self._data[key] = value
    def set(self, key, value):
        self._data[key] = value
    def get(self, key):
        # make sure there is no KeyError
        return self._data.get(key)
    def __getitem__(self, key):
        return self._data[key]
    def __setitem__(self, key, value):
        self._data[key] = value
    def __delitem__(self, key):
        del self._data[key]
    def __contains__(self, key):
        return key in self._data
    