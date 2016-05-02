import logging

from rpyc.utils.server import ThreadPoolServer

logger = logging.getLogger(__name__)

class RPyCServer(ThreadPoolServer):
    """ Threaded RPC server to handle connections from implants. """

    def __init__(self, *args, **kwargs):
        ThreadPoolServer.__init__(self, *args, **kwargs)
