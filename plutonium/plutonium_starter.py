import os, sys

from plutonium.modules.logger import load_logger, get_logger
from plutonium.modules.config import Config
from plutonium.modules.tools import FileReader
from plutonium.modules.plutonium_class import Plutonium

# get the user's home
base_working_dir = os.path.join(os.path.expanduser('~'), '.plutonium')

load_logger(os.path.join(base_working_dir, 'config', 'logger.json'))

logger = get_logger('plutonium')

logger.info("Welcome to the world's most wonderful bittorrent rss fetcher. (pid: %d)" % os.getpid())

# init config
try:
    config = Config(FileReader())
    config.load(os.path.join(base_working_dir, 'config', 'core.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)

# create instance
plutonium = Plutonium(config)

# start the command server, and block this thread
plutonium.start_command_server()

# bye
logger.info("Plutonium has been stopped gracefully")