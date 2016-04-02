import argparse
import logging

logger = logging.getLogger(__name__)

class MyParserException(Exception):
    pass

class CrispyArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
	argparse.ArgumentParser.__init__(self, *args, **kwargs)

    def error(self, message):
	""" Override method to prevent argparse from calling sys.exit() """
	logger.error("CrispyArgumentParser error")
	self.print_usage()
	raise MyParserException
