class Entry:
    def __init__(self, entry_data, config):
        self.config = config
        self.url = entry_data.link
        self.title = entry_data.title
        self.description = entry_data.description
        self.published =entry_data.published
        self.apply_config()

    def apply_config(self):
        for attribute in self.config.attributes:
            if hasattr(self, attribute):
                continue

            value = self.config.get_value(self.title, attribute)
            setattr(self, attribute, value)

    def to_csv(self):
        out = []
        for attribute in self.config.attributes:
            out.append(getattr(self, attribute))
        return out
