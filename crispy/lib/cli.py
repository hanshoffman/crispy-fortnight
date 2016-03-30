import argparse
import cmd
import ConfigParser
import getpass
import logging
import sys

from crispy import __version__

logger = logging.getLogger(__name__)

BANNER = "                                                                     \n \
     ___           ___                       ___           ___                 \n \
    /  /\         /  /\        ___          /  /\         /  /\         ___    \n \
   /  /:/        /  /::\      /  /\        /  /:/_       /  /::\      /__/|    \n \
  /  /:/        /  /:/\:\    /  /:/       /  /:/ /\     /  /:/\:\    |  |:|    \n \
 /  /:/  ___   /  /:/~/:/   /__/::\      /  /:/ /::\   /  /:/~/:/    |  |:|    \n \
/__/:/  /  /\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/\:\ /__/:/ /:/   __|__|:|    \n \
\  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/~/:/ \  \:\/:/   /__/::::\    \n \
 \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/ /:/   \  \::/       ~\~~\:\   \n \
  \  \:\/:/     \  \:\          /__/:/    \__\/ /:/     \  \:\         \  \:\  \n \
   \  \::/       \  \:\         \__\/       /__/:/       \  \:\         \__\/  \n \
    \__\/         \__\/                     \__\/         \__\/                \n \
								       %s" %(__version__)

class CrispyCLI(cmd.Cmd):
    """ Available commands for crispy cli. """

    def __init__(self, srv, config_file="crispy.conf"):
	cmd.Cmd.__init__(self)
	self.config = ConfigParser.ConfigParser()
	self.config.read(config_file)
	if self.config.getboolean("CMDLINE", "display_banner"):
	    self.intro = BANNER
	else:
	    self.intro = ""
	self.prompt="{0}@crispy>> ".format(getpass.getuser())
	self.doc_header = "Available commands:"
	self.srv = srv

    def do_EOF(self, args):
	""" Use Ctrl-D (i.e. EOF) to exit. """
        logger.debug("Ctrl-D received... shutting down crispyd")
	print ""
        sys.exit()

    def do_help(self, args):
	""" Help menu. """
	logger.debug("do_help() was called")
	cmd.Cmd.do_help(self, args)

    def emptyline(self):
	""" Do nothing when an emptyline is entered. """
	pass

    def do_modules(self, args):
	""" List available modules. """
	pass

    def do_sessions(self, args):
	""" List/interact with established sessions. """
	logger.debug("do_sessions() was called")
	print "implement me"
    
    def do_run(self, args):
	""" Run a module on one or multiple clients. """
	logger.debug("do_run() was called")
	print "implement me"
