
import thread

from timer import Timer
from tools import SimpleResponse, URLLoader
from modules.commands import external_jsonrpc_command, commandline

from feed import Feed
from filter import Filter
from output import Output

class Fetcher(object):

    def __init__(self, config, logger, orm_manager, plugin_manager):
        self.config = config
        self.logger = logger
        self.orm_manager = orm_manager
        self.plugin_manager = plugin_manager
        self.feeds = []

    def do_fetch(self):
        for feed in self.feeds:
            feed.fetch()

    @external_jsonrpc_command
    @commandline('Fetch the feeds now')
    def fetch(self):
        thread.start_new_thread(self.do_fetch, ())
        return SimpleResponse(True, 'Fetching started in %d feed(s)' % len(self.feeds))

    def add_torrents(self, torrents):
        session = self.orm_manager.create_session()
        # SQLAlchemy's ORM does not supports bulk insert. But the typical size of the torrents param ~2-3, so not a bug problem...
        for torrent in torrents:
            session.add(torrent)
        session.commit()

    def init_models(self):

        # init Output
        if 'output' not in self.plugin_manager.plugins:
            self.logger.warning('There is no output plugin configured!')
            return

        Output.output_plugins = self.plugin_manager.plugins['output']

        # init Feed
        Feed.url_loader = URLLoader()

    def get_output_types(self):
        if 'output' not in self.plugin_manager.plugins:
            self.logger.warning('There is no output plugin configured!')
            return

        plugins = self.plugin_manager.plugins['output']

        return plugins.keys()

    def fetch_feeds_from_database(self):
        self.feeds = []
        for feed in self.orm_manager.create_session().query(Feed).all():
            self.feeds.append(feed)
            feed.set_fetcher(self)

    def stop(self):
        for feed in self.feeds:
            feed.stop()

    def start(self):
        for feed in self.feeds:
            feed.start()
