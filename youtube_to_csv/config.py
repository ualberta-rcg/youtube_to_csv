import yaml

class Config:
    CSV_HEADER = [
        'URL',
        'Title',
        'Description',
        'Licence',
        'Status',
        'Author',
        'Published',
        'Keywords',
        'Types',
        'Competency',
        'Prerequisites'
    ]

    def __init__(self, config_file_yml):
        self._config = self.load_config(config_file_yml)

    def load_config(self, config_file_yml):
        with open(config_file_yml, "r") as file:
            return yaml.safe_load(file)

    @property
    def url(self):
        return self._config['url']

    @property
    def attributes(self):
        return list(map(lambda x: x.lower(), self.CSV_HEADER))

    @property
    def csv_header(self):
        return self.CSV_HEADER

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
