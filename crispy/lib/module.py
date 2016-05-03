import logging

logger = logging.getLogger(__name__)

from abc import abstractmethod

class CrispyModule(object):
    """ Module object that all other modules will inherit from. """
    
    def __init__(self, client):
        self.client = client

    def check_args(self, args):
        """ Override this method to define your own arguments. """
        logger.debug("check_args(args) was called.")

    def is_compatible(self):
        """ Override this method to define if module is compatible with the given client. """
        logger.debug("is_compatible() was called.")

        if "all" in self.compatible_systems:
            return True
        elif "Windows" in self.compatible_systems and self.client.is_windows():
            return True
        elif "Linux" in self.compatible_systems and self.client.is_linux():
            return True
        elif "Darwin" in self.compatible_systems and self.client.is_darwin():
            return True
        elif "Unix" in self.compatible_systems and self.client.is_unix():
            return True
        else:
            return False

    @abstractmethod
    def run(self):
        """ Override this method for each module to perform it's own actions. """
        pass
