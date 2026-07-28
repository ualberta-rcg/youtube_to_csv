import yaml

class Config:
    COLUMNS_REQUIRED = [
        'URL',
        'Title',
        'Description'
    ]

    def __init__(self, config_file_yml):
        self._config = self.load_config(config_file_yml)
        self._csv_header = None

    def load_config(self, config_file_yml):
        with open(config_file_yml, "r") as file:
            return yaml.safe_load(file)

    @property
    def url(self):
        return self._config['url']

    @property
    def attributes(self):
        return list(map(lambda x: x.lower(), self.csv_header))

    @property
    def columns(self):
        return self._config.get('columns', [])

    @property
    def csv_header(self):
        if not self._csv_header:
            self._csv_header = self.COLUMNS_REQUIRED.copy()
            for column in self.columns:
                if column not in self._csv_header:
                    self._csv_header.append(column)

        return self._csv_header

    @property
    def defaults(self):
        return self._config['defaults']

    @property
    def video_values(self):
        return self._config['video_values']

    def get_value(self, title, attribute):
        values = self.video_values.get(title)
        if values:
            out = values.get(attribute)
            if out:
                return out
        out = self.defaults.get(attribute)
        if out:
            return out
