import logging 
import rpyc.core.service
import sys

logger = logging.getLogger(__name__)

from .. lib.fprint import *

class CrispyService(rpyc.Service):
    def __init__(self, *args, **kwargs):
        super(CrispyService, self).__init__(*args, **kwargs)
        self.srv = global_srv

    def on_connect(self):
        logger.debug("on_connect() was called")
       
        try:
            self._conn._config.update(dict(
                allow_safe_attrs = True,
                allow_public_attrs = False,
                allow_pickle = False,
                allow_getattr = True,
                allow_delattr = False,
                allow_setattr = False,
                import_custom_exceptions = False,
                instantiate_custom_exceptions = False,
                instantiate_oldstyle_exceptions = False,
            ))
            self.builtin = None
            self.eval = self._conn.root.eval
            self.execute = self._conn.root.execute
            self.exit = self._conn.root.exit
            self.exposed_stdin = sys.stdin
            self.exposed_stdout = sys.stdout
            self.exposed_stderr = sys.stderr
            self.modules = None
            self.namespace = self._conn.root.namespace

            self.srv.add_client(self)
        except Exception as e:
            error(e)
        
    def on_disconnect(self):
        logger.debug("on_disconnect() was called")

        self.srv.remove_client(self)

    def exposed_set_modules(self, modules):
        logger.debug("set_modules() was called")

        self.modules = modules
        self.builtin = self.modules.__builtin__
