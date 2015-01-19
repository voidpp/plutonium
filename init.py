#!/usr/bin/env python

import os, sys

sys.path.extend(['modules', 'models'])

from logger import get_logger
from config import Config
from modules.commands import CommandRequestHandler
from cliargumentstreeparser import CLIArgumentsTreeParser
from tools import FileReader
from plutonium_manager import PlutoniumManager

# import the classes with 'commandline' decorated functions! (maybe not used the class, but need to import)
from modules.plutonium import Plutonium
from modules.fetcher import Fetcher

cwd = os.getcwd()

# init argument parsing
control_command = dict(name = 'control', desc = dict(help = 'Commands for the running Plutonium core'), subcommands = [])

args_config = [
    dict(name = 'start', desc = dict(help = 'Start Plutonium')),
    dict(name = 'stop', desc = dict(help = 'Stop Plutonium')),
    dict(name = 'restart', desc = dict(help = 'Restart Plutonium')),
    dict(name = 'status', desc = dict(help = 'The status of Plutonium')),
    control_command,
]

# get the rpc method list to add args
for name in dir(CommandRequestHandler):
    attr = getattr(CommandRequestHandler, name)
    if hasattr(attr, 'commandline'):
        cmd_desc = attr.commandline
        control_command['subcommands'].append(dict(name = name, desc = dict(help = cmd_desc.help), arguments = cmd_desc.arguments))

parser = CLIArgumentsTreeParser(args_config, 'core')
args = parser.parse()


# init logger
logger = get_logger(os.path.join(cwd, 'config', 'logger.json'), 'init')
logger.info("Plutonium manager script")


# init config
try:
    config = Config(FileReader(), logger)
    config.load(os.path.join(cwd, 'config', 'core.json'))
    logger.info('Config has been successfully loaded')
except Exception as e:
    logger.error('Exception occured during config parsing: ' + str(e))
    sys.exit(1)


# create manager
mgr = PlutoniumManager(config.data['command_server']['port'].value, os.path.join(cwd, 'plutonium.pid'), logger)
command = getattr(mgr, args.sub.name)
command_args = args.sub.sub if 'sub' in args.sub else dict()
response = command(**command_args)
logger.info(response.message)
