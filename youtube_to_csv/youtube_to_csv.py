import csv
import feedparser
import sys

from .entry import Entry
from .config import Config

class YoutubeToCSV:
    def __init__(self, config_file_yml=None):
        self.config = Config(config_file_yml)
        self._feed = None
        self._entries = None

    @property
    def url(self):
        return self.config.url

    @property
    def entries(self):
        if not self._entries:
            self._entries = []
            for entry_data in self.feed.entries:
                self._entries.append(Entry(entry_data, self.config))

        return self._entries

    @property
    def feed(self):
        if not self._feed:
            self._feed = feedparser.parse(self.url)

        return self._feed

    @property
    def csv_header(self):
        return self.config.csv_header

    def run(self):
        writer = csv.writer(sys.stdout, lineterminator="\n")
        writer.writerow(self.csv_header)
        for entry in self.entries:
            writer.writerow(entry.to_csv())
