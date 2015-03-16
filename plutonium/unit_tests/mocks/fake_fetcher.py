
from fetcher import Fetcher

class FakeFetcher(Fetcher):

    def fetch(self):
        pass

    def add_torrent(self, torrent, commit = False):
        pass

    def commit(self):
        pass

    def init_models(self):
        pass

    def get_output_types(self):
        pass

    def fetch_feeds_from_database(self):
        pass

    def stop(self):
        pass

    def start(self):
        pass
