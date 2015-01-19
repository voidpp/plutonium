import os, sys

sys.path.extend(['modules', 'models'])

from logger import get_logger
from config import Config
from tools import FileReader
from modules.plutonium import Plutonium

cwd = os.getcwd()

# init logger
logger = get_logger(os.path.join(cwd, 'config', 'logger.json'), 'core')
logger.info("Welcome to the world's most wonderful bittorrent rss fetcher. (pid: %d)" % os.getpid())

# init config
try:
    config = Config(FileReader(), logger)
    config.load(os.path.join(cwd, 'config', 'core.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)

# create instance
plutonium = Plutonium(config, logger)

# start the command server, and block this thread
plutonium.start_command_server()

# bye
logger.info("Plutonium has been stopped gracefully")
