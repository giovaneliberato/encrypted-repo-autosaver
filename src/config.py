import json


class ConfigManager:
    CONFIG_FILE = 'resources/configs.json'

    def __init__(self):
        self._config = self._load()

    def _load(self):
        with open(self.CONFIG_FILE, 'r') as config:
            return json.loads(config.read())

    def _write(self):
        with open(self.CONFIG_FILE, 'w') as config:
            config.write(json.dumps(self._config))

    def put(self, key, value):
        self._config.put(key, value)
        self._write()

    def get(self, key):
        return self._config.get(key)
